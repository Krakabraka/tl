ttd = []
memory = {}
def runshell(thing):
  if thing.startswith("output "):
    thing = thing.replace("output ", "")
    secondc = thing.split(" ")
    for sc in secondc:
      sc2 = list(sc)
      coloncount = 0
      for char in sc2:
        if char == ":":
          coloncount += 1
      if coloncount == 2:
        thing = thing.replace(sc, str(memory[sc.replace(":", "")]))
    secondc = thing.split(" ")
    for sc in secondc:
      sc = str(sc)
      if sc.startswith("(") and sc.endswith(")"):
        evalsc = str(eval(sc))
        thing = thing.replace(sc, evalsc)
    print(thing)
  elif thing.startswith("input "):
    thing = thing.replace("input ", "")
    thing = thing.split(" ")
    fv = str(thing[1:len(thing)])
    fv = fv.replace("['", "")
    fv = fv.replace("']", "")
    fv = fv.replace("', '", " ")
    fv = input(fv)
    memory[thing[0]] = fv
  elif thing.startswith("if "):
    thing = thing.replace("if ", "")
    secondc = thing.split(" ")
    for sc in secondc:
      sc2 = list(sc)
      coloncount = 0
      for char in sc2:
        if char == ":":
          coloncount += 1
      if coloncount == 2:
        thing = thing.replace(sc, str(memory[sc.replace(":", "")]))
    secondc = thing.split(" ")
    for sc in secondc:
      sc = str(sc)
      if sc.startswith("(") and sc.endswith(")"):
        evalsc = str(eval(sc))
        thing = thing.replace(sc, evalsc)
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
        secondc = toexec.split(" ")
        for sc in secondc:
          sc2 = list(sc)
          coloncount = 0
          for char in sc2:
            if char == ":":
              coloncount += 1
          if coloncount == 2:
            toexec = toexec.replace(sc, str(memory[sc.replace(":", "")]))
        secondc = toexec.split(" ")
        for sc in secondc:
          sc = str(sc)
          if sc.startswith("(") and sc.endswith(")"):
            evalsc = str(eval(sc))
            toexec = toexec.replace(sc, evalsc)
        print(toexec)
      elif toexec.startswith("input "):
        toexec = toexec.replace("input ", "")
        toexec = toexec.split(" ")
        fv = str(toexec[1:len(toexec)])
        fv = fv.replace("['", "")
        fv = fv.replace("']", "")
        fv = fv.replace("', '", " ")
        fv = input(fv)
        memory[toexec[0]] = fv
      elif " = " in toexec:
        toexec = toexec.split(" = ")
        fv = str(toexec[1:len(toexec)])
        fv = fv.replace("['", "")
        fv = fv.replace("']", "")
        fv = fv.replace("', '", " ")
        memory[toexec[0]] = fv
    if ifcheck[0] != ifcheck[1] and has_else:
      if elsecheck.startswith("output "):
        elsecheck = elsecheck.replace("output ", "")
        secondc = elsecheck.split(" ")
        for sc in secondc:
          sc2 = list(sc)
          coloncount = 0
          for char in sc2:
            if char == ":":
              coloncount += 1
          if coloncount == 2:
            elsecheck = elsecheck.replace(sc, str(memory[sc.replace(":", "")]))
        secondc = elsecheck.split(" ")
        for sc in secondc:
          sc = str(sc)
          if sc.startswith("(") and sc.endswith(")"):
            evalsc = str(eval(sc))
            elsecheck = elsecheck.replace(sc, evalsc)
        print(elsecheck)
      elif elsecheck.startswith("input "):
        elsecheck = elsecheck.replace("input ", "")
        elsecheck = elsecheck.split(" ")
        fv = str(elsecheck[1:len(elsecheck)])
        fv = fv.replace("['", "")
        fv = fv.replace("']", "")
        fv = fv.replace("', '", " ")
        fv = input(fv)
        memory[elsecheck[0]] = fv
      elif " = " in elsecheck:
        elsecheck = elsecheck.split(" = ")
        fv = str(elsecheck[1:len(elsecheck)])
        fv = fv.replace("['", "")
        fv = fv.replace("']", "")
        fv = fv.replace("', '", " ")
        memory[elsecheck[0]] = fv
  elif thing.startswith("repeat "):
    thing = thing.replace("repeat ", "")
    thing = thing.split(" | ")
    repeater = thing[0]
    toexec = thing[1]
    for i in range(int(repeater)):
      runshell(toexec)
  elif " = " in thing:
    thing = thing.split(" = ")
    fv = str(thing[1:len(thing)])
    fv = fv.replace("['", "")
    fv = fv.replace("']", "")
    fv = fv.replace("', '", " ")
    memory[thing[0]] = fv
def runfile(thing):
  thing = thing.readlines()
  for c in thing:
    c = c.replace("\n", "")
    if c.startswith("output "):
      c = c.replace("output ", "")
      secondc = c.split(" ")
      for sc in secondc:
        sc2 = list(sc)
        coloncount = 0
        for char in sc2:
          if char == ":":
            coloncount += 1
        if coloncount == 2:
          c = c.replace(sc, str(memory[sc.replace(":", "")]))
      secondc = c.split(" ")
      for sc in secondc:
        sc = str(sc)
        if sc.startswith("(") and sc.endswith(")"):
          evalsc = str(eval(sc))
          c = c.replace(sc, evalsc)
      print(c)
    elif c.startswith("input "):
      c = c.replace("input ", "")
      c = c.split(" ")
      fv = str(c[1:len(c)])
      fv = fv.replace("['", "")
      fv = fv.replace("']", "")
      fv = fv.replace("', '", " ")
      fv = input(fv)
      memory[c[0]] = fv
    elif c.startswith("if "):
      c = c.replace("if ", "")
      secondc = c.split(" ")
      for sc in secondc:
        sc2 = list(sc)
        coloncount = 0
        for char in sc2:
          if char == ":":
            coloncount += 1
        if coloncount == 2:
          c = c.replace(sc, str(memory[sc.replace(":", "")]))
      secondc = c.split(" ")
      for sc in secondc:
        sc = str(sc)
        if sc.startswith("(") and sc.endswith(")"):
          evalsc = str(eval(sc))
          c = c.replace(sc, evalsc)
      c = c.split(" | ")
      ifcheck = c[0]
      toexec = c[1]
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
          secondc = toexec.split(" ")
          for sc in secondc:
            sc2 = list(sc)
            coloncount = 0
            for char in sc2:
              if char == ":":
                coloncount += 1
            if coloncount == 2:
              toexec = toexec.replace(sc, str(memory[sc.replace(":", "")]))
          secondc = toexec.split(" ")
          for sc in secondc:
            sc = str(sc)
            if sc.startswith("(") and sc.endswith(")"):
              evalsc = str(eval(sc))
              toexec = toexec.replace(sc, evalsc)
          print(toexec)
        elif toexec.startswith("input "):
          toexec = toexec.replace("input ", "")
          toexec = toexec.split(" ")
          fv = str(toexec[1:len(toexec)])
          fv = fv.replace("['", "")
          fv = fv.replace("']", "")
          fv = fv.replace("', '", " ")
          fv = input(fv)
          memory[toexec[0]] = fv
        elif " = " in toexec:
          toexec = toexec.split(" = ")
          fv = str(toexec[1:len(toexec)])
          fv = fv.replace("['", "")
          fv = fv.replace("']", "")
          fv = fv.replace("', '", " ")
          memory[toexec[0]] = fv
      if ifcheck[0] != ifcheck[1] and has_else:
        if elsecheck.startswith("output "):
          elsecheck = elsecheck.replace("output ", "")
          secondc = elsecheck.split(" ")
          for sc in secondc:
            sc2 = list(sc)
            coloncount = 0
            for char in sc2:
              if char == ":":
                coloncount += 1
            if coloncount == 2:
              elsecheck = elsecheck.replace(sc, str(memory[sc.replace(":", "")]))
          secondc = elsecheck.split(" ")
          for sc in secondc:
            sc = str(sc)
            if sc.startswith("(") and sc.endswith(")"):
              evalsc = str(eval(sc))
              elsecheck = elsecheck.replace(sc, evalsc)
          print(elsecheck)
        elif elsecheck.startswith("input "):
          elsecheck = elsecheck.replace("input ", "")
          elsecheck = elsecheck.split(" ")
          fv = str(elsecheck[1:len(elsecheck)])
          fv = fv.replace("['", "")
          fv = fv.replace("']", "")
          fv = fv.replace("', '", " ")
          fv = input(fv)
          memory[elsecheck[0]] = fv
        elif " = " in elsecheck:
          elsecheck = elsecheck.split(" = ")
          fv = str(elsecheck[1:len(elsecheck)])
          fv = fv.replace("['", "")
          fv = fv.replace("']", "")
          fv = fv.replace("', '", " ")
          memory[elsecheck[0]] = fv
    elif c.startswith("repeat "):
      c = c.replace("repeat ", "")
      c = c.split(" | ")
      repeater = c[0]
      toexec = c[1]
      for i in range(int(repeater)):
        runshell(toexec)
    elif " = " in c:
      c = c.split(" = ")
      fv = str(c[1:len(c)])
      fv = fv.replace("['", "")
      fv = fv.replace("']", "")
      fv = fv.replace("', '", " ")
      memory[c[0]] = fv
while True:
  command = input("> ")
  if command == "tl start":
    for c in ttd:
      if c.startswith("run "):
        c = c.replace("run ", "")
        c = c + ".tl"
        with open(f"{c}") as file:
          runfile(file)
      elif c.startswith("open "):
        c = c.replace("open ", "")
        with open(f"{c}") as file:
          c = file.read()
          print(c)
      else:
        runshell(c)
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