extends CharacterBody2D

@export var SPEED = 70.0
@export var FIRE_DURATION = 1.0
@export var AIM_SPREAD_DEGREES = 25.0

@onready var _animated_sprite = $AnimatedSprite2D
@onready var _aim_overlay = $AimOverlay

var is_firing = false
var fire_timer = 0.0
var last_direction = Vector2.RIGHT

func _ready():
    _aim_overlay.visible = false

func _physics_process(delta: float) -> void :
    var input_direction: = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")

    if input_direction != Vector2.ZERO:
        last_direction = input_direction

    if is_firing:
        _face_mouse()
        _update_aim_overlay()
        velocity = Vector2.ZERO
        fire_timer -= delta
        if fire_timer <= 0:
            is_firing = false
            _aim_overlay.visible = false
            _fire_arrow()

    else:
        _aim_overlay.visible = false
        velocity = input_direction * SPEED

        if input_direction != Vector2.ZERO:
            _animated_sprite.play("walk")
            if input_direction.x != 0:
                _animated_sprite.flip_h = input_direction.x < 0
        else:
            _animated_sprite.play("idle")

    move_and_slide()

func _input(event):
    if event is InputEventMouseButton:
        if event.button_index == MOUSE_BUTTON_LEFT and event.pressed and not is_firing:
            is_firing = true
            fire_timer = FIRE_DURATION
            _animated_sprite.play("fire")
            _aim_overlay.visible = true


func _face_mouse():
    var mouse_pos = get_global_mouse_position()
    var to_mouse = (mouse_pos - global_position).normalized()

    if to_mouse.x != 0:
        _animated_sprite.flip_h = to_mouse.x < 0

func _update_aim_overlay():
    var mouse_pos = get_global_mouse_position()
    var direction = (mouse_pos - global_position).normalized()


    _aim_overlay.global_position = global_position + direction


    _aim_overlay.rotation = direction.angle()
    _aim_overlay.spread_degrees = AIM_SPREAD_DEGREES

func _fire_arrow():
    var mouse_pos = get_global_mouse_position()
    var base_dir = (mouse_pos - global_position).normalized()


    var spread_rad = deg_to_rad(AIM_SPREAD_DEGREES)
    var random_angle = randf_range( - spread_rad, spread_rad)
    var final_dir = base_dir.rotated(random_angle).normalized()


    if final_dir.x != 0:
        _animated_sprite.flip_h = final_dir.x < 0

    var arrow_scene = preload("res://scenes/arrow.tscn")
    var arrow = arrow_scene.instantiate()
    get_tree().current_scene.add_child(arrow)
    arrow.global_position = global_position
    arrow.direction = final_dir
