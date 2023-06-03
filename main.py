from scrapper import web_scrapper


web_scrapper(40, 'zachodniopomorskie.csv',
            'https://www.booking.com/searchresults.pl.html?ss=zachodniopomorskie&ssne=zachodniopomorskie&ssne_untouched=zachodniopomorskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=1563&dest_type=region&checkin=2023-07-10&checkout=2023-07-17&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
             False)

#
# web_scrapper(14, 'lubuskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=lubuskie%2C+Polska&ssne=zachodniopomorskie&ssne_untouched=zachodniopomorskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=1979&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=503b574c129e0214&ac_meta=GhA1MDNiNTc0YzEyOWUwMjE0IAAoATICcGw6CGx1YnVza2llQABKAFAA&checkin=2023-07-17&checkout=2023-07-24&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(40, 'dolnoslaskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=dolno%C5%9Bl%C4%85skie%2C+Polska&ssne=lubuskie&ssne_untouched=lubuskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=1306&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=dae457609e080304&ac_meta=GhBkYWU0NTc2MDllMDgwMzA0IAAoATICcGw6BWRvbG5vQABKAFAA&checkin=2023-07-10&checkout=2023-07-17&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(9, 'opolskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=opolskie%2C+Polska&ssne=dolno%C5%9Bl%C4%85skie&ssne_untouched=dolno%C5%9Bl%C4%85skie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=2227&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=f5ea57755b8503ac&ac_meta=GhBmNWVhNTc3NTViODUwM2FjIAAoATICcGw6CG9wb2xza2llQABKAFAA&checkin=2023-07-03&checkout=2023-07-10&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
#
#
# web_scrapper(2, 'pomorskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=pomorskie%2C+Polska&ssne=opolskie&ssne_untouched=opolskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=1308&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=f5755785694f018f&ac_meta=GhBmNTc1NTc4NTY5NGYwMThmIAAoATICcGw6BXBvbW9yQABKAFAA&checkin=2023-07-03&checkout=2023-07-10&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(38, 'wielkopolskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=wielkopolskie%2C+Polska&ssne=pomorskie&ssne_untouched=pomorskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=1309&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=bac1579a04cd0300&ac_meta=GhBiYWMxNTc5YTA0Y2QwMzAwIAEoATICcGw6BXdpZWxrQABKAFAA&checkin=2023-07-03&checkout=2023-07-10&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(31, 'kujawsko_pomorskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=kujawsko-pomorskie%2C+Polska&ssne=wielkopolskie&ssne_untouched=wielkopolskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=2226&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=4&search_selected=true&search_pageview_id=d60557a772400049&ac_meta=GhBkNjA1NTdhNzcyNDAwMDQ5IAAoATICcGw6Emt1amF3c2tvX3BvbW9yc2tpZUAASgBQAA%3D%3D&checkin=2023-07-10&checkout=2023-07-17&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(22, 'lodzkie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=%C5%82%C3%B3dzkie%2C+Polska&ssne=kujawsko-pomorskie&ssne_untouched=kujawsko-pomorskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=2306&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=4&search_selected=true&search_pageview_id=290657b7a96603ad&ac_meta=GhAyOTA2NTdiN2E5NjYwM2FkIAEoATICcGw6B2xvZHpraWVAAEoAUAA%3D&checkin=2023-07-10&checkout=2023-07-17&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
#
#
# web_scrapper(40, 'slaskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=%C5%9Bl%C4%85skie%2C+Polska&ssne=%C5%82%C3%B3dzkie&ssne_untouched=%C5%82%C3%B3dzkie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=1562&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=dd0557cfddc101ce&ac_meta=GhBkZDA1NTdjZmRkYzEwMWNlIAAoATICcGw6A3NsYUAASgBQAA%3D%3D&checkin=2023-07-03&checkout=2023-07-10&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(40, 'warminsko_mazurskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=warmi%C5%84sko-mazurskie%2C+Polska&ssne=%C5%9Bl%C4%85skie&ssne_untouched=%C5%9Bl%C4%85skie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=2224&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=f80a57dc6f450208&ac_meta=GhBmODBhNTdkYzZmNDUwMjA4IAAoATICcGw6Bndhcm1pbkAASgBQAA%3D%3D&checkin=2023-07-03&checkout=2023-07-10&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(40, 'mazowieckie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=mazowieckie%2C+Polska&ssne=warmi%C5%84sko-mazurskie&ssne_untouched=warmi%C5%84sko-mazurskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=1310&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=6d9457e8018700fe&ac_meta=GhA2ZDk0NTdlODAxODcwMGZlIAEoATICcGw6B21hem93aWVAAEoAUAA%3D&checkin=2023-07-03&checkout=2023-07-10&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(20, 'swietokrzyskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=%C5%9Bwi%C4%99tokrzyskie%2C+Polska&ssne=mazowieckie&ssne_untouched=mazowieckie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=1881&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b41057f525a601e3&ac_meta=GhBiNDEwNTdmNTI1YTYwMWUzIAAoATICcGw6BnN3aWV0b0AASgBQAA%3D%3D&checkin=2023-07-10&checkout=2023-07-17&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
#
#
#
# web_scrapper(40, 'malopolskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=ma%C5%82opolskie%2C+Polska&ssne=%C5%9Bwi%C4%99tokrzyskie&ssne_untouched=%C5%9Bwi%C4%99tokrzyskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=1307&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=a49758005af50073&ac_meta=GhBhNDk3NTgwMDVhZjUwMDczIAAoATICcGw6BW1hbG9wQABKAFAA&checkin=2023-07-17&checkout=2023-07-24&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(36, 'podlaskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=podlaskie%2C+Polska&ssne=ma%C5%82opolskie&ssne_untouched=ma%C5%82opolskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=2225&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=79525838dd0300e7&ac_meta=GhA3OTUyNTgzOGRkMDMwMGU3IAAoATICcGw6BnBvZGxhc0AASgBQAA%3D%3D&checkin=2023-07-03&checkout=2023-07-10&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(32, 'lubelskie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=lubelskie%2C+Polska&ssne=podlaskie&ssne_untouched=podlaskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=1762&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=9e3558438caa001d&ac_meta=GhA5ZTM1NTg0MzhjYWEwMDFkIAAoATICcGw6BWx1YmVsQABKAFAA&checkin=2023-07-03&checkout=2023-07-10&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)
#
#
# web_scrapper(40, 'podkarpackie.csv',
#             'https://www.booking.com/searchresults.pl.html?ss=podkarpackie%2C+Polska&ssne=lubelskie&ssne_untouched=lubelskie&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=2228&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=pl&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=c5ec584eab4d001e&ac_meta=GhBjNWVjNTg0ZWFiNGQwMDFlIAAoATICcGw6BXBvZGthQABKAFAA&checkin=2023-07-10&checkout=2023-07-17&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&age=10',
#              False)