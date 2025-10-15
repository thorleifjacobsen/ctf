extends Node

@onready var label_equation = $equation
@onready var targets = $Targets
@onready var gandalf = $Gandalf
@onready var animated_sprite = gandalf.get_child(1)

var result = 0
var resetting = false

func create_equiation() -> Array[int]:
    var a = randi_range(4, 17)
    var b = randi_range(4, 17)
    while a * b > 255:
        b = randi_range(5, 17)
    return [a, b]

func _ready() -> void :
    _generate_new_equation()

func _generate_new_equation():
    var a = create_equiation()
    label_equation.text = str(a[0]) + " x " + str(a[1])
    result = a[0] * a[1]

func reset_ept_trining_game():
    if resetting:
        return
    resetting = true
    animated_sprite.play("wand_slam")
    await get_tree().create_timer(1.5).timeout
    _finish_reset()

func _process(delta: float) -> void :
    if resetting:
        return

    var targets_list = targets.get_children()
    var i = 0
    var res = String.num_int64(result, 2).pad_zeros(8)

    var correct = 0
    for target in targets_list:
        if not target.is_fire_on and res[i] == "1":

            SignalBus.emit_signal("display_dialog", "gandalf_failed")
            reset_ept_trining_game()
            break
        elif (target.is_fire_on and res[i] == "1") or ( not target.is_fire_on and res[i] == "0"):
            correct += 1
        i += 1
    if correct == 8:
        print("YOU WON")
        SignalBus.emit_signal("display_dialog", "gandalf_won")
        reset_ept_trining_game()

func _finish_reset():
    _generate_new_equation()
    for target in targets.get_children():
        target.is_fire_on = true
    animated_sprite.play("idle")
    resetting = false
