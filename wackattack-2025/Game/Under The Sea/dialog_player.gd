extends CanvasLayer

func hex_string_to_byte_array(hex_str: String) -> PackedByteArray:
    var byte_array = PackedByteArray()
    for hex in hex_str.split(","):
        byte_array.append(hex.hex_to_int())
    return byte_array

func xor_byte_arrays_to_string(a: PackedByteArray, b: PackedByteArray) -> String:
    if a.size() != b.size():
        print("Byte arrays must be of the same size!")
        return ""

    var result = PackedByteArray()
    for i in range(a.size()):
        result.append(a[i] ^ b[i])

    return result.get_string_from_utf8()

func xor(a: PackedByteArray, b: PackedByteArray) -> PackedByteArray:
    if a.size() != b.size():
        print("Byte arrays must be of the same size!")
        return PackedByteArray()

    var result = PackedByteArray()
    for i in range(a.size()):
        result.append(a[i] ^ b[i])

    return result


var scene_text = {
    "gandalf": [
        {text = "Urggg... I can\'t get this right!"}, 
        {text = "I\'m training for the cyber range. Can you do it?"}, 
        {text = "Do the math, convert to binary..."}, 
        {text = "you get the flag!"}
    ], 
    "gandalf_won": [
        {text = "You did it!..."}, 
        {text = "You won!!! Here is the flag as reward..."}, 
        {text = "wack{b3st_sh00t3r_3vr}"}
    ], 
    "gandalf_failed": [
        {text = "No no no! That\'s all wrong! Try again!", skip_after_sec = 2}
    ], 
    "gjort_det_igjen": [
        {text = "Vi fant skatten igjen!"}
    ], 
    "sign_broken_bridge": [
        {text = "The bridge is closed due to mantinence."}, 
        {text = "- WackConstruction AS"}
    ], 
    "old_man": [
        {text = "My back hurts!"}, 
        {text = "When I was young...\nI ran like the wind!"}, 
        {text = "Got to train for onsite challs!"}
    ], 
    "sign_remote_island": [
        {text = "2c,6a,3d,1f,72,fe,c5,ba,d3,26,f7,49,67,5b,ba,83,85,a8,f6,9c,31,23,18,cc,7c,b2,7b,8b,db,24,68,e3,8b,73,5c,a7,27,30,41,50,87,00,9a", xor = "0e,5e,0b,21,5c,cd,fc,96,d9,1b,c3,7f,59,51,98,b7,bc,91,fc,a1,05,15,26,c6,46,95,71,ad,e1,1c,58,c2,b6,4f,67,95,2d,00,78,76,b7,6a,b2"}, 
    ], 
    "wack_world_sign": [
        {text = "Welcome to WackWorld!"}, 
        {text = "A place of where flags recide"}
    ], 
    "worker": [
        {text = "Howdy!"}
    ], 
    "sign_bottom_island": [
        {text = "Legends say there are wild flags living under the water\'s surface"}
    ]
}

var selected_text = []
var in_progress = false

@onready var background = $ColorRect2
@onready var text_label = $ColorRect2 / Label
@onready var timer = $Timer

func _ready():
    background.visible = false
    SignalBus.connect("display_dialog", on_display_dialog)
    SignalBus.connect("hide_dialog", finish)
    timer.connect("timeout", _on_timer_timeout)

func show_text():
    var text_entry = selected_text.pop_front()
    var text_to_display = text_entry.text
    if text_entry.has("xor"):
        var bytes1 = hex_string_to_byte_array(text_entry.text)
        var bytes2 = hex_string_to_byte_array(text_entry.xor)
        var bytes3 = hex_string_to_byte_array("55,".repeat(42).rpad(1, ","))
        var first = xor(bytes2, bytes3)
        text_to_display = xor_byte_arrays_to_string(bytes1, first)

    text_label.text = text_to_display


    var time_to_wait = text_entry.get("skip_after_sec", 7)
    timer.start(time_to_wait)

func next_line():
    if selected_text.size() > 0:
        show_text()
    else:
        finish()

func finish():
    text_label.text = ""
    background.visible = false
    in_progress = false
    timer.stop()

func on_display_dialog(text_key):
    if in_progress:
        next_line()
    else:
        background.visible = true
        in_progress = true
        selected_text = scene_text[text_key].duplicate()
        show_text()

func _on_timer_timeout():

    next_line()
