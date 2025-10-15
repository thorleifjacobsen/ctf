extends StaticBody2D

@onready var sprite = $AnimatedSprite2D

func _ready() -> void :
    sprite.play("idle")



func _process(delta: float) -> void :
    pass
