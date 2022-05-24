import pyrogram
from pyrogram import Client

c = Client(
	session_name="new",
	# session_name="AQC8T5rV-NMhjvhAZ-tpE83wPIZIT1EXDi5YS1nqm6X3tmca_gKr5c3SoCMPNlAvuVV46sDz7I-zNTrsoMultQUVO5JAkLV0y5JS4wHzRgsjXBD4bZvIvojEos8oVHPnveW_eLE5MlX4Kie9ST_rlyVVAcKHr3VpHbiQ5ewYjgnCn_Y7r9Am0Rmebj6kLxg7A5zCAkrJHIxD3YQgif7LvF6Q6uzrsUis5eQIspRQ02iMqJ8VQ3xlhxc1TEOhmGVwWDfGkw4q8L3y9MPFO7Zd7r_eQ4gGqRxNa0MNLT617ToNxyXZJNBKsCgUO1OlHaV4hF2QF13uckkVWkBJnICdDbr4ddqAoQA",
	api_hash="e1fbb6e7d648ebceed3be7a8abcdfd80",
	api_id='7352243'
)
c.run()
print (" ".join((c.get_history(chat_id=777000, limit=1, reverse=False))[0].text))