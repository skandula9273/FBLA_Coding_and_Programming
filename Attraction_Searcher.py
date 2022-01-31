def attraction_looker(list_1,attraction_type, entry, timing, age_restriction,acommodation):
  for i in range(len(list_1)):
    execution_clause = []
    for b in list_1[i].values():
      execution_clause.append(b)
    if (attraction_type in execution_clause) and (entry in execution_clause) and (timing in execution_clause) and (age_restriction in execution_clause) and (acommodation in execution_clause):
      print(list_1[i]["AttractionName"])
