extends Path2D

@onready var pathfollow = $PathFollow2D
@onready var sprite = $PathFollow2D / AnimatableBody2D / AnimatedSprite2D
var lastx = 0

func _ready() -> void :
    sprite.play("walk")

func _process(delta: float) -> void :
    pass
    if lastx > pathfollow.position.x:
        sprite.flip_h = true
    else:
        sprite.flip_h = false
    lastx = pathfollow.position.x

func _physics_process(delta: float) -> void :
    const move_speed = 15.0
    pathfollow.progress += move_speed * delta
