import spiceypy
import datetime

date_today = datetime.datetime.today()
datre_time = date_today.strftime("%Y-%m-%dT00:00:00")
# print(date_today)

spiceypy.furnsh("/workspaces/Space-Science-Projects/kernels/lsk/naif0012.tls")
# spiceypy.furnsh(/kernels/lsk/naif0012.tls")
# spiceypy.furnsh("./kernels/spk/de432s.bsp")