extends StaticBody2D

@onready var _animated_sprite = $AnimatedSprite2D


func _ready() -> void :
    _animated_sprite.play("idle")


func _process(delta: float) -> void :
    pass
