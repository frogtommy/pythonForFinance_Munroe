def doSimpleCalculations():
    var1 = 99999#  create variable equal to 99999
    var2 = 11111#  create variable equal to 11111
    return(var1/var2)#  return first variable divided by the second one


def combineStringsSimple():
  uofu = "University of "#  create variable Univerisity of
  utah = "Utah "#  create variable Utah
  rule = "Rules"#  create variable Rules
  return (uofu+utah+rule)#   return University of Utah Rules


def combineNumsStrings():
  num = 32000#  create number variable 32000
  uofu2 = "University of Utah has "#  create variable University of Utah has
  student = " students"#  create variable students
  return (uofu2 + str(num) + student)#  combine all of the variables so you would get University of Utah has 32000 students


def convertStringToNum(paramOne):
    print(paramOne)
    converted = float(paramOne)
    return converted/50