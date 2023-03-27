import base64

skall0 = "ICAgICAgICAgICBfLCxnZywsXyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIF8sLGdnLCxfCiAgICAgICAgLGE4ODhQODhZODg4YSwgICAgICAgICAg"
skall1 = "ICAgICAgICAgICAgICAgICAsYTg4OFA4OFk4ODhhLAogICAgICAsZCI4IjgiLFlZLCI4IjgiYiwgICAgICAgICAgICAgICAgICAgICAgICxkIjgiOCIsWVksIjgi"
skall2 = "OCJiLAogICAgIGQiLFAnZCcgZCdgYiBgYmBZLCJiLCAgICAgICAgICAgICAgICAgICAgZCIsUCdkJyBkJ2BiIGBiYFksImIsCiAgICxQIixQJyxQICA4ICA4ICBZ"
skall3 = "LGBZLCJZLCAgICAgICAgICAgICAgICAgLFAiLFAnLFAgIDggIDggIFksYFksIlksCiAgLFAgLFAnIGQnICA4ICA4ICBgYiBgWSwgWSwgICAgICAgICAgICAgICAs"
skall4 = "UCAsUCcgZCcgIDggIDggIGBiIGBZLCBZLAogLFAgLFBfLCw4Z2dnOGdnOGdnZzgsLF9ZLCBZLCAgICAgICAgICAgICAsUCAsUF8sLDhnZ2c4Z2c4Z2dnOCwsX1ks"
skall5 = "IFksCiw4UCIiIiIiIiInJyAgICAgIGBgIiIiIiIiIlk4LCAgICAgICAgICAgLDhQIiIiIiIiIicnICAgICAgYGAiIiIiIiIiWTgsCmQnL35cICAgIC9+XCAgICAv"
skall6 = "flwgICAgL35cICBgYiAgICAgICAgICAgZCcgLGE4YSwgICAgL1wgL1wgICAgLGE4YSwgIGBiCjgvICAgXCAgLyAgIFwgIC8gICBcICAvICAgXCAgOCAgICAgICAg"
skall7 = "ICAgOCAsUCIgIlksICAgICggKSAgICAsUCIgIlksICA4CjggLDgsIFwvICw4LCBcLyAsOCwgXC8gLDgsIFwvOCAgICAgICAgICAgOCxQJyAgIGBZLCAuKCBvICku"
skall8 = "ICxQJyAgIGBZLCA4CjggIlkiIC9cICJZIiAvXCAiWSIgL1wgIlkiIC9cOCAgICAgICAgICAgOFAnL1wgL1xgWSwgICBfICAgLFAnL1wgL1xgWSw4CjhcICAgLyAg"
skall9 = "XCAgIC8gIFwgICAvICBcICAgLyAgOCAgICAgICAgICAgOCcgICggKSAgYFksIChfKSAsUCcgICggKSAgYFk4CjggXF8vICAgIFxfLyAgICBcXy8gICAgXF8vICAg"
skallA = "OCAgICAgICAgICAgOCAuKCBvICkuIGBZYSAgIGFQJyAuKCBvICkuIGA4CjggICAgICAgICAgICAgICAgICAgICAgICAgICAgOCAgICAgICAgICAgOCA9LT0tPS09"
skallB = "ICAgIllhUCIgICA9LT0tPS09ICA4ClkiIiIiWVlZYWFhYSwsLCwsLGFhYWFQUFAiIiIiUCAgICAgICAgICAgWSIiIiJZWVlhYWFhLCwsLCwsYWFhYVBQUCIiIiJQ"
skallC = "CmBiIGFnLCAgIGBgIiIiIiIiIiInJyAgICxnYSBkJyAgICAgICAgICAgYGIgYWcsICAgYGAiIiIiIiIiIicnICAgLGdhIGQnCiBgWVAgImIsICAsYWEsICAsYWEs"
skallD = "ICAsZCIgWVAnICAgICAgICAgICAgIGBZUCAiYiwgICxhYSwgICxhYSwgICxkIiBZUCcKICAgIlksXyJZYSxfKTggIDgoXyxhUCJfLFAiICAgICAgICAgICAgICAg"
skallE = "ICAiWSxfIllhLF8pOCAgOChfLGFQIl8sUCIKICAgICBgIllhXyIiIiAgICAiIiJfYVAiJyAgICAgICAgICAgICAgICAgICAgIGAiWWFfIiIiICAgICIiIl9hUCIn"
skallF = "CiAgICAgICAgYCIiWVliYmRkUFAiIicgICAgICAgICAgICAgICAgICAgICAgICAgICBgIiJZWWJiZGRQUCIiJw=="
skall = skall0 + skall1 + skall2 + skall3 + skall4 + skall5 + skall6 + skall7 + skall8 + skall9 + skallA + skallB + skallC + skallD + skallE + skallF
red_herring = "helsectf{ ... }"
eggeskall = skall

Eggeplomme2 = '            __  __  __ __  __  __          __           __ '
Eggeplomme3 = '|\/| /\ |  |  \/  \/  /  \|__)|__)\  / /\ |__)|\/|||\ |/ _ '
Eggeplomme1 = '|  |/--\|__|__/\__/\__\__/|   |    \/ /--\| \ |  ||| \|\__)'

eggehvite = '                  _ /'
eggehvite = eggehvite + Eggeplomme2
eggehvite = eggehvite + '\\ '
eggehvite = eggehvite + "\n" + '|_  _ | _ _  _ |_(_( '
eggehvite = eggehvite + Eggeplomme3
eggehvite = eggehvite + '  )' + "\n"
eggehvite = eggehvite + '| )(-`|_)(-`(_ |_|  \\'
eggehvite = eggehvite + Eggeplomme1 + "/ "
# Else
# eggehvite = "                  _ /"
# eggehvite = eggehvite + "                                                           " + "\ "
# eggehvite = eggehvite + "\n" + "|_  _ | _ _  _ |_(_( "
# eggehvite = eggehvite + "                                                          " + "  )" + "\n"
# eggehvite = eggehvite + "| )(-`|_)(-`(_ |_|  \\"
# eggehvite = eggehvite + "                                                           " + "/ "
# End If

# End Function
# Function Eggeplomme(i As Integer)

# Select Case i
#     Case 3
#         Eggeplomme1 = "|  |/--\|__|__/\__/\__\__/|   |    \/ /--\| \ |  ||| \|\__)"
#     Case 1
#         Eggeplomme2 = "            __  __  __ __  __  __          __           __ "
#     Case 2
#         Eggeplomme3 = "|\/| /\ |  |  \/  \/  /  \|__)|__)\  / /\ |__)|\/|||\ |/ _ "

# End Select

# print(base64.b64decode(eggeskall).decode())
print()
print(eggehvite)
print()
# print(base64.b64decode(eggeskall).decode())


# print( DecodeBase64(eggeskall) + vbCrLf + eggehvite; vbCrLf; DecodeBase64(eggeskall)
