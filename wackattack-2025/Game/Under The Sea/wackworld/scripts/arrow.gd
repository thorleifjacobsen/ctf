extends Area2D

@export var SPEED = 250.0
var direction = Vector2.ZERO

func _process(delta: float) -> void :
    if direction != Vector2.ZERO:
        position += direction.normalized() * SPEED * delta
        rotation = direction.angle()

func _on_area_entered(area):
    print("I hit something!")
    queue_free()
