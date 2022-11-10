ttd = []
memory = {}
def format(thing):
  secondc = thing.split(" ")
  for sc in secondc:
    sc2 = list(sc)
    coloncount = 0
    for char in sc2:
      if char == ";":
        coloncount += 1
      if coloncount == 2:
        sc = str(sc)
        sc2 = sc
        sc = sc.split(";")
        if len(sc) == 1:
          sc = sc[0].split("', '")
          thing = thing.replace(sc[1].replace(";", ""), str(memory[sc[1]])).replace(";", "")
        else:
          thing = thing.replace(sc[1].replace(";", ""), str(memory[sc[1]])).replace(";", "")
  secondc = thing.split(" ")
  for sc in secondc:
    sc = str(sc)
    if sc.startswith("(") and sc.endswith(")"):
      evalsc = str(eval(sc))
      thing = thing.replace(sc, evalsc)
  return thing
def run(thing):
  if thing.startswith("output "):
    thing = thing.replace("output ", "")
    thing = format(thing)
    print(thing)
  elif thing.startswith("input "):
    thing = thing.replace("input ", "")
    thing = thing.split(" = ")
    fv = str(thing[1])
    fv = format(fv)
    fv = input(fv)
    memory[thing[0]] = fv
  elif thing.startswith("if "):
    thing = thing.replace("if ", "")
    thing = format(thing)
    thing = thing.split(" | ")
    ifcheck = thing[0]
    toexec = thing[1]
    elsecheck = None
    has_else = False
    try:
      elsecheck = c[2]
      has_else = True
    except IndexError:
      has_else = False
    ifcheck = ifcheck.split(" = ")
    if str(ifcheck[0]) == str(ifcheck[1]):
      if toexec.startswith("output "):
        toexec = toexec.replace("output ", "")
        toexec = format(toexec)
        print(toexec)
      elif toexec.startswith("input "):
        toexec = toexec.replace("input ", "")
        toexec = toexec.split(" = ")
        fv = str(toexec[1])
        fv = format(fv)
        fv = input(fv)
        memory[toexec[0]] = fv
      elif " = " in toexec:
        toexec = toexec.split(" = ")
        fv = str(toexec[1])
        fv = format(fv)
        memory[toexec[0]] = fv
    if ifcheck[0] != ifcheck[1] and has_else:
      if elsecheck.startswith("output "):
        elsecheck = elsecheck.replace("output ", "")
        elsecheck = format(elsecheck)
        print(elsecheck)
      elif elsecheck.startswith("input "):
        elsecheck = elsecheck.replace("input ", "")
        elsecheck = elsecheck.split(" = ")
        fv = str(elsecheck[1])
        fv = format(fv)
        fv = input(fv)
        memory[elsecheck[0]] = fv
      elif " = " in elsecheck:
        elsecheck = elsecheck.split(" = ")
        fv = str(elsecheck[1])
        fv = format(fv)
        memory[elsecheck[0]] = fv
  elif thing.startswith("repeat "):
    thing = thing.replace("repeat ", "")
    thing = thing.split(" | ")
    repeater = thing[0]
    toexec = thing[1]
    for i in range(int(repeater)):
      run(toexec)
  elif " = " in thing:
    thing = thing.split(" = ")
    fv = str(thing[1])
    fv = format(fv)
    memory[thing[0]] = fv
while True:
  command = input("> ")
  if command.lower() == "tl start":
    for c in ttd:
      if c.startswith("run "):
        c = c.replace("run ", "")
        c = c + ".tl"
        with open(f"{c}") as file:
          file = file.readlines()
          for c in file:
            c = c.replace("\n", "")
            run(c)
      elif c.startswith("open "):
        c = c.replace("open ", "")
        with open(f"{c}") as file:
          c = file.read()
          print(c)
      else:
        run(c)
    ttd = []
  elif command == "tl undo":
    ttd.pop(len(ttd) - 1)
  elif command.startswith("tl debug "):
    command = command.replace("tl debug ", "")
    print(eval(command))
  elif command == "tl showinstructions":
    print(ttd)
  elif command == "tl showvariables":
    print(memory)
  else:
    ttd.append(command)
