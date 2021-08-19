impor rpa as r
array_items = []
csv_file = 'taguiemails.csv'
lines = r.load(csv_file)
array_lines = lines.split('\n')
r.init()
r.url('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
for n in array_lines:
    r.click('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]')
    r.type('email',n)
    r.type('//*[@name="subjectbox"]','Hi')
    r.type('//*[@class="Am Al editable LW-avf tS-tW"]','Hello')
    r.click('//*[@class="T-I J-J5-Ji aoO v7 T-I-atl L3"]')
r.close()
