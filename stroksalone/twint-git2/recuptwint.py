import twint

c = twint.Config()

c.Username = "enceinte"
c.Limit = 1
c.Store_csv = True
c.Output = "Strape"

twint.run.Search(c)
