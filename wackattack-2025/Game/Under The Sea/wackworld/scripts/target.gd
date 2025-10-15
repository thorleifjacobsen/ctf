extends Area2D

@onready var _animated_sprite = $AnimatedSprite2D
@export var is_fire_on: bool = true

func _ready() -> void :
    _animated_sprite.play("fire")

func _process(delta: float) -> void :
    if is_fire_on:
        _animated_sprite.play("fire")
    else:
        _animated_sprite.play("no_fire")

func _on_area_entered(area: Area2D) -> void :
    if area.is_in_group("arrow"):
        is_fire_on = false
        _animated_sprite.play("no_fire")
