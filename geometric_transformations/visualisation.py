import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox
from calculations import *

accum_matrix = np.eye(3)

pts_original = star_points(center=(0, 0), outer_radius=5, inner_radius=2)
sq_original = bounding_square(pts_original)
pts_original = transform(pts_original, rotation_matrix(np.pi/2))
sq_original = transform(sq_original, rotation_matrix(np.pi/2))

fig, ax = plt.subplots(figsize=(15,10))
plt.subplots_adjust(left=0.1, bottom=0.35)

ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')
ax.grid(True)

ax.plot(pts_original[:, 0], pts_original[:, 1], 'gray', linestyle='--', linewidth=1, label='Исходная звезда')
ax.plot(sq_original[:, 0], sq_original[:, 1], 'gray', linestyle=':', linewidth=1, label='Исходный квадрат')

line_star, = ax.plot([], [], 'b-', linewidth=2, label='Преобразованная звезда')
line_square, = ax.plot([], [], 'r--', linewidth=1.5, label='Преобразованный квадрат')
ax.legend(loc='upper right')

init_angle = 0
init_scale_x = 1.0
init_scale_y = 1.0
init_trans_x = 0.0
init_trans_y = 0.0

def compute_matrix(angle_deg, sx, sy, tx, ty):
    angle_rad = np.radians(angle_deg)
    R = rotation_matrix(angle_rad)
    S = scaling_matrix(sx, sy)
    T = translation_matrix(tx, ty)
    return T @ R @ S

def update(val=None):
    angle = s_angle.val
    sx = s_scalex.val
    sy = s_scaley.val
    tx = s_transx.val
    ty = s_transy.val

    M_sliders = compute_matrix(angle, sx, sy, tx, ty)
    M_total = accum_matrix @ M_sliders

    pts_trans = transform(pts_original, M_total)
    sq_trans = transform(sq_original, M_total)

    line_star.set_data(pts_trans[:, 0], pts_trans[:, 1])
    line_square.set_data(sq_trans[:, 0], sq_trans[:, 1])

    text_angle.set_val(f"{angle:.1f}")
    text_scalex.set_val(f"{sx:.2f}")
    text_scaley.set_val(f"{sy:.2f}")
    text_transx.set_val(f"{tx:.1f}")
    text_transy.set_val(f"{ty:.1f}")

    fig.canvas.draw_idle()

color = 'lightgoldenrodyellow'

slider_height = 0.03
slider_y_start = 0.25
slider_gap = 0.02

ax_angle = plt.axes([0.2, slider_y_start, 0.6, slider_height], facecolor=color)
s_angle = Slider(ax_angle, 'Угол (град)', -180, 180, valinit=init_angle, valstep=1)

ax_scalex = plt.axes([0.2, slider_y_start - slider_gap, 0.6, slider_height], facecolor=color)
s_scalex = Slider(ax_scalex, 'Масштаб X', 0.2, 3.0, valinit=init_scale_x, valstep=0.1)

ax_scaley = plt.axes([0.2, slider_y_start - 2*slider_gap, 0.6, slider_height], facecolor=color)
s_scaley = Slider(ax_scaley, 'Масштаб Y', 0.2, 3.0, valinit=init_scale_y, valstep=0.1)

ax_transx = plt.axes([0.2, slider_y_start - 3*slider_gap, 0.6, slider_height], facecolor=color)
s_transx = Slider(ax_transx, 'Сдвиг X', -15, 15, valinit=init_trans_x, valstep=0.5)

ax_transy = plt.axes([0.2, slider_y_start - 4*slider_gap, 0.6, slider_height], facecolor=color)
s_transy = Slider(ax_transy, 'Сдвиг Y', -15, 15, valinit=init_trans_y, valstep=0.5)

s_angle.on_changed(update)
s_scalex.on_changed(update)
s_scaley.on_changed(update)
s_transx.on_changed(update)
s_transy.on_changed(update)

textbox_width = 0.1
textbox_height = 0.02
textbox_x_start = 0.82
textbox_y = slider_y_start - 0.01

ax_text_angle = plt.axes([textbox_x_start, textbox_y, textbox_width, textbox_height])
text_angle = TextBox(ax_text_angle, '', initial=f"{init_angle:.1f}")

ax_text_scalex = plt.axes([textbox_x_start, textbox_y - slider_gap, textbox_width, textbox_height])
text_scalex = TextBox(ax_text_scalex, '', initial=f"{init_scale_x:.2f}")

ax_text_scaley = plt.axes([textbox_x_start, textbox_y - 2*slider_gap, textbox_width, textbox_height])
text_scaley = TextBox(ax_text_scaley, '', initial=f"{init_scale_y:.2f}")

ax_text_transx = plt.axes([textbox_x_start, textbox_y - 3*slider_gap, textbox_width, textbox_height])
text_transx = TextBox(ax_text_transx, '', initial=f"{init_trans_x:.1f}")

ax_text_transy = plt.axes([textbox_x_start, textbox_y - 4*slider_gap, textbox_width, textbox_height])
text_transy = TextBox(ax_text_transy, '', initial=f"{init_trans_y:.1f}")

def submit_angle(val):
    try:
        a = float(val)
        s_angle.set_val(a)
    except ValueError:
        pass

def submit_scalex(val):
    try:
        sx = float(val)
        s_scalex.set_val(sx)
    except ValueError:
        pass

def submit_scaley(val):
    try:
        sy = float(val)
        s_scaley.set_val(sy)
    except ValueError:
        pass

def submit_transx(val):
    try:
        tx = float(val)
        s_transx.set_val(tx)
    except ValueError:
        pass

def submit_transy(val):
    try:
        ty = float(val)
        s_transy.set_val(ty)
    except ValueError:
        pass

text_angle.on_submit(submit_angle)
text_scalex.on_submit(submit_scalex)
text_scaley.on_submit(submit_scaley)
text_transx.on_submit(submit_transx)
text_transy.on_submit(submit_transy)

reset_ax = plt.axes([0.25, 0.12, 0.1, 0.04])
button_reset = Button(reset_ax, 'Сброс', color=color, hovercolor='0.975')

reflectx_ax = plt.axes([0.35, 0.12, 0.1, 0.04])
button_reflect_ox = Button(reflectx_ax, 'Ox', color=color, hovercolor='0.975')

reflecty_ax = plt.axes([0.45, 0.12, 0.1, 0.04])
button_reflect_oy = Button(reflecty_ax, 'Oy', color=color, hovercolor='0.975')

reflectyx_ax = plt.axes([0.55, 0.12, 0.1, 0.04])
button_reflect_yx = Button(reflectyx_ax, 'y = x', color=color, hovercolor='0.975')

def reset_all(event):
    global accum_matrix
    accum_matrix = np.eye(3)
    s_angle.set_val(0)
    s_scalex.set_val(1.0)
    s_scaley.set_val(1.0)
    s_transx.set_val(0)
    s_transy.set_val(0)

def apply_reflection(R):
    global accum_matrix
    accum_matrix = R @ accum_matrix
    update()

def apply_rotation(event):
    global accum_matrix
    
    px = float(text_rotation_point_x.text)
    py = float(text_rotation_point_y.text)
    angle = float(text_angle_box.text)
    angle = np.radians(angle)
    print(angle)
    accum_matrix = rotation_point_matrix(px, py, angle) @ accum_matrix
    update()

ax_angle_text_box = plt.axes([0.25, 0.06, 0.1, 0.04])
text_angle_box = TextBox(ax_angle_text_box, '', initial="0")

ax_rotation_point_x = plt.axes([0.35, 0.06, 0.1, 0.04])
ax_rotation_point_y = plt.axes([0.45, 0.06, 0.1, 0.04])
text_rotation_point_x = TextBox(ax_rotation_point_x, '', initial="0")
text_rotation_point_y = TextBox(ax_rotation_point_y, '', initial="0")

ax_submit = plt.axes([0.55, 0.06, 0.1, 0.04])
submit_button = Button(ax_submit, 'Применить')

button_reflect_ox.on_clicked(lambda x: apply_reflection(reflection_Ox_matrix()))
button_reflect_oy.on_clicked(lambda x: apply_reflection(reflection_Oy_matrix()))
button_reflect_yx.on_clicked(lambda x: apply_reflection(reflection_yx_matrix()))
button_reset.on_clicked(reset_all)
submit_button.on_clicked(apply_rotation)

update()
plt.show()