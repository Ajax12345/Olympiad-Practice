def end_other(a, b):
  if a[len(a)-len(b):].lower() == b.lower() or b[len(b)-len(a):].lower() == a.lower():
    return True
    
  else:
    return False
    
if __name__ == "main":
   string1 = 'Hiabc'
   string2 = 'abc'
   
   flag = end_other(string1, string2)
   if flag:
      print "string2 appears on the end of string1"
      
   else:
      print "string2 does not appear on the end of string1"
