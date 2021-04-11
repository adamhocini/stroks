import twint

c = twint.Config()

c.Username = "lemondefr"
c.Limit = 10
c.Store_csv = True
c.Output = "Strape"
c.Search = "maternité"

twint.run.Search(c)
