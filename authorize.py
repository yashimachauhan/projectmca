def authriseuser(auth,role,userrole):
    try:
        if(auth==True):
            if(role==userrole):
                return True
            else:
                return False,"Wrong User"
        else:
            return False,"Not Login"
    except:
        return False, "Not Login"
