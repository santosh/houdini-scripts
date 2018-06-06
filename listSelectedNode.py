# print full paths to selected node in DAG
selected = hou.selectedNodes()

buff = ["No nodes selected" if len(selected) < 1 else sel.path() + "\n" for sel in selected]

hou.ui.displayMessage("".join(buff), buttons=("Got it!",), title="Selected Nodes")