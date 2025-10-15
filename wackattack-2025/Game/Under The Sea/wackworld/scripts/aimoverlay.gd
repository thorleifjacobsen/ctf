extends Node2D

@export var radius = 50
@export var spread_degrees = 10.0

func _draw():
    var spread_rad = deg_to_rad(spread_degrees)
    draw_arc(Vector2.ZERO, radius, - spread_rad, spread_rad, 3, Color(1, 1, 1, 0.2), 2)

func _process(_delta):
    queue_redraw()
