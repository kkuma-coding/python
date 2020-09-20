# Make a function gerund_infinitive that, given a string ending in "ing",
# returns the rest of the string prefixed with "to ". If the string
# doesn't end in "ing", return "That's not a gerund!"
#
# >>>> gerund_infinitive("building")
# to build
# >>>> gerund_infinitive("build")
# That's not a gerund!

def gerund_infinitive(string):
    if "ing" == string[-3:]:
        # print (string, "은 동명사!")
        print ("to", string[:-3:])
    else:
        print (string, "은 동명사 아님!")

# Add more statements to test what your function does:
gerund_infinitive("building")
# cooking  : 요리 중
# building : 집 짓는 중
gerund_infinitive("build")

gerund_infinitive("cooking")
gerund_infinitive("cook")

gerund_infinitive("reading")
gerund_infinitive("read")