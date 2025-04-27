from flask import Flask, render_template

app = Flask(__name__)

# Курсы и предметы
courses = [
    {
        "name": "1.Klasse",
        "subjects": [
            {"name": "AM", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EgKGi_hRvWhGjnaljE52SdwBhHuZ4b0vk1UjGl8gy6whxA?e=hzV3k0"},
            {"name": "BET", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EltntO02FWtNuCyopJGaVboB7YtRSQ2g0WBwInz46j4rdg?e=aOQ3Ga"},
            {"name": "Deutsch", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Er-HMm-wu0pAiS0lNMCIYiABmFlTxEvGvajfkiHdznTb9A?e=q5LNaC"},
            {"name": "DG", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Eq-N_YOnIVFGuvR7C6RVLyoBxk8siBQh9YX0K-tPS3bY_Q?e=MnrTzz"},
            {"name": "Englisch", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EglK56RGawFHkaidT6fZI8YBrOYMG8f03kMpfDj87-18-w?e=4XO2ea"},
            {"name": "ETAUT", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Et3o2d8d7TNAmyfu4bsgsWoBm1cwOOUGfPPAMxGKdMZFhA?e=ALsw1p"},
            {"name": "GGP", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EgO-tWikCZFNnnLxy6n0-ewBb7keUWDA-sMlJmXcOY-BEQ?e=4Qb92p"},
            {"name": "INFI", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/ElqG1ddTYF5Kn00bufQmNx0BjGQoZP8hvCVSw9OoMGRrog?e=h05rP9"},
            {"name": "KODES", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Etbf_DDNfZBDpz_ppy5QD4ABPOamEOodf4an5iZHwFIz8g?e=3pbEko"},
            {"name": "Physik", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EoPNJ8_DHg9PmbHwWwgCoawBFdBpDOb1nCotIiRqmea8lQ?e=q8RfRo"},
            {"name": "Protwe", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EmbqNqSlr-hCtTydf56zFxYBQ3mqDARntblCPyPuN51OVA?e=hTAohO"},
            {"name": "Religion", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EowYNEEPsh1MrR8lSprocc8BQk6T2l0IIFVs7eBEcJOHMw?e=p5gjyy"}
        ]
    },
    {
        "name": "2.Klasse",
        "subjects": [
            {"name": "AM", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EkmXiZ-p2kVJiYaTINjKG9ABA8XSKImfUJLSRD27az1dFQ?e=xhYB3C"},
            {"name": "BET", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EiCgzjrJZWVGjRCizKyG24ABNKniWtgXmFrWSBo2lYx8wQ?e=O6cZh3"},
            {"name": "Chemie", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Eobi3wqWqGdKhM5wlRiRuZQBmowzBq_D_lPqWRRA35hYug?e=VEDPdn"},
            {"name": "CS", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Ep5WNOyY_qVAkSq9qSoKO8wB5M6wMY5-NsE8DjY0DTWI-w?e=eOguFh"},
            {"name": "Deutsch", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EjSZNEWwjKhCieUDNodyNvcB-ScYJ8f8ePTBFONceZd33w?e=ziu1Mn"},
            {"name": "Englisch", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EvE4THGxasZDpew4OX3geO4BPZj_TSPLJtHq5k8zbfSzTA?e=J9kR5x"},
            {"name": "ETAUT", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EtzO8HHz2qNHpXqfRZrNOFsBthMChBNmJqnIF_PRz-WqZA?e=fhW9k2"},
            {"name": "GGP", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Ei_o8gpcphhJl0rcKagew7IBYnJSjQ9bKTx74RK3-Sdf5g?e=sjFG6B"},
            {"name": "INFI", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EitY0YrhyAlItSxNO6v6yucBcLlzmdF-YJjl2hEX701lXw?e=ggatOZ"},
            {"name": "KODES", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EpRTHQPDmG9NictNFs-nAs4BYl1M1qb-YPTTehSqIU-rvA?e=boCEgd"},
            {"name": "MME", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EnXV-Ufn9FZCi4EWIQ2pfRoBLZED6Y42mpPcBPSZ18jodg?e=7VzXaz"},
            {"name": "PROTWE", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EraMuf28cf9Hoyo1J4FBz7IB7wrpEc69zjQjobac-iKUrw?e=KcjvEu"},
            {"name": "Religion", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Epyol5i07kNJo8PoxK42jmUB7MotDUY4tb3ej8GJZ4Nyow?e=lUwHgF"},
            {"name": "UFW", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Elfsb_kuE65ChYHOohJTXqUBCKFpw9ssSsSSiqEagdbMzQ?e=VwXtvF"}
        ]
    },
    {
        "name": "3.Klasse",
        "subjects": [
            {"name": "AM", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Et_gKIMkzvZOndsgrif2HO4BCd1g6ONy0n6hImL5Tak7Fg?e=LcGEaa"},
            {"name": "BET", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EnTMsH6AMZtMoAMzuqkNTBcBST8gOzwtQlGaTRTlK5aYuQ?e=6fYU9Z"},
            {"name": "Chemie", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EuxXZXAS8KlKoko-vlvfFM0B6RWYL9ErFsGbi0fuHvZnuw?e=Rb7X6x"},
            {"name": "Deutsch", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EqVoiQSFZW1ApxSsWr0XMVsBR_1PyjnGpSqAnXu7-bAdMw?e=eHdVv5"},
            {"name": "Englisch", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EjEEjgaRvYRDg5A0YAzblPcBUGpuZfwbJUnMjSJUyy5dVA?e=cWcZlo"},
            {"name": "ETAUT", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EkKSYiPzdeNKooTO0r1h8PsBuchC6SDGCrT9LX4gzg3nig?e=h3oqxc"},
            {"name": "Geografie", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EgA4AkZfAt1Aqv-6xdKkFasBSOq5HjT7RlC2Ne560ZGE-Q?e=3x2XnY"},
            {"name": "Geschichte", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/ErTN1OwAJFxMvEdOSHUSZ5QBskMBD2MpC6_KRUWTGOZ0-A?e=EjlztN"},
            {"name": "INFI", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EhjTHXdiAEVEiE7a-gWzPHwBnLIsp9guTDRnn_Uz7M7YjA?e=bFmXTp"},
            {"name": "MME", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EuQru8uUtPhDhgyT6dPXfQ4B4ZRHZgwSoFn43ZkVq36KkQ?e=Zyecd3"},
            {"name": "MMEM", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/El9GGLAW-vZEt9XX48T6TkEBPwDcQFTHRDZw1jicstJGhg?e=RWFuQ0"},
            {"name": "Physik", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EsrwTTYvERtApTN2esyC-LwB_A_z6y0fT47MGazaO82AGA?e=5bTRq9"},
            {"name": "Protwe", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EjOIaUe4oWlNvLIS-oPhW-cBeDo3h52TrTG5Azldfmngdg?e=UqjdEV"},
            {"name": "Religion", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EhPfC9gs1XtGsaU4zI5e9PUBbVCpIs_06xFl8pj0Ve8YSQ?e=AehTeo"},
            {"name": "UFW", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Ei-rHywiLV5LleZMTyK75O4BQQUDnOosNMMdBJB1YjSKXw?e=CcGNbe"}
        ]
    },
    {
        "name": "4.Klasse",
        "subjects": [
            {"name": "AM", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EsT07BxyWflEvJvKvtKN-D0B5__PnOWdN15NcPyKk-P7aw?e=Dk7Yk8"},
            {"name": "BET", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Eg2kIPWj6mtFrRYvthukEpgBXJIP-yOmR9j9Dou_ZRpehg?e=ULGlXU"},
            {"name": "CAENG", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EpVzSm1VyM1Aoyvw3sdFruEBTaJoI_b5R2KUaVLyb4szlw?e=xfEIWb"},
            {"name": "Chemie", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Eg6W1HjlH8xIg6fzv3Dqz6oB70lM4r4ktgF7eu-IH3gv0w?e=aWRfTf"},
            {"name": "CS", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/ErSOU8qm619ChZosn7V8m7gBoUsH9t86v2cKgN33lNR6Ng?e=82b3XH"},
            {"name": "Deutsch", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EoiQKm_k0hNFpKk5FdMdhT0BejpZ4j1fi5VxOrtB0QjDOw?e=2sF21B"},
            {"name": "Englisch", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EvfUu32HrxlKrjEMLt7Jv4sBQ0xb5OtBbKwFojOYGgOR0A?e=2gCnBp"},
            {"name": "Geografie", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EhT-ip201kZOg6F-l_lhlgcBg0zG1ccWCmEprhNOfh3qxQ?e=e7d4us"},
            {"name": "Geschichte", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EndCyZ-LBkNLvGZqny60KN0BFUMH8UEx-lKMyDUFvyMXkA?e=o8b3d7"},
            {"name": "INFI", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EoJ2korWia5ApII7AXKx5HQBWJSzmzFA5ysRUrCfopaWZg?e=WqwMJb"},
            {"name": "KODES", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EoJHQndAOYBCmbQGn44hu8EBAunfYSb3lD9pb4U_dEIEIw?e=l6IKJ6"},
            {"name": "MME", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Ek8QH67sw3pPuhMJuvdYWIUBf_j8qvR-XHJ3_Cf7o9Ufkw?e=ejLcZk"},
            {"name": "Physik", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Ejxhf3gVA2lKt0QGCZ7-TJEBcC0VUCmCFySKcq8GKjr8Tw?e=Fz57Gr"},
            {"name": "PROLAW", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EnRV8lZqFGRFiOOgN9bv0OYBiBj1A8s7DguFVlR-EpCPYw?e=hNQRyM"},
            {"name": "Protwe", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EkKoWRKrGpBHjGRO0nWIfT8BZKAjAMYM_5BF7iUmWjb9nw?e=ez9GD9"},
            {"name": "Religion", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Ekm6szrpX7lOuLZRQ8zFfowBbxN5PEA5nnFLo9I861PxGA?e=8ZAoUE"},
            {"name": "SUINE", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EhVDfKHXhdNJrWo2RDF-VpEBmRrRu_lx8dzwc_21s7rUWg?e=PXstyV"},
            {"name": "UFW", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Es8psiUy7EFAuNUA4fL1RZEBBbUFX-opUiilVADds5oJ8Q?e=uXKnDY"}
        ]
    },
    {
        "name": "5.Klasse",
        "subjects": [
            {"name": "AM", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EqANxnpypEJOlOyMqy92jksByA9YyQ2jvzKO917Dm1-RUw?e=ck8bpc"},
            {"name": "BET", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EhULQXm3pyRHqwDwGV0iYX8BFJrBNO1-kxv-CgxyKVJDng?e=UxHyda"},
            {"name": "Deutsch", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EvTs_GLabrNOhAYbnyOLEcsBgDlK0EUz8HaNXfKG2_V57A?e=MxjXWJ"},
            {"name": "Englisch", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/Eku7KSiedpxPhCQXP9f6g1gBIh2HkTZXP3IXhybGxTJmbw?e=yl5jjz"},
            {"name": "INFI", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EqWgLPRyIb9KgJWRIsjysW0BjQ1q6o5LM2TsnTaaerxhSA?e=KJltGv"},
            {"name": "MAA", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EiZTLDhDaUJDuXa3IOm3oE0BNw5gf-3AXwMoLLkk55yGqg?e=vplIVT"},
            {"name": "PROLAW", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EgllzP9Oo35CtbJ_nl7kHmUBoj0ukxjbVq2S9XpHELrLJw?e=wTSi7E"},
            {"name": "Religion", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EmIZO6v6onBAkDWCOdx9MNEB4632FrPkboWduQiLYDNYhQ?e=tvKYaw"},
            {"name": "UFW", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EgtrMKewfMFHjUKZXOEZ978BxZvHi3PitIvwRP_8zx1JfQ?e=NtpY3N"},
            {"name": "WSFT", "url": "https://htlmd365-my.sharepoint.com/:f:/g/personal/20222594_htl-md_schule/EiURNbsMt4lJiPe7j1V9XfQBvPqDAk1qHgIv7m0XGxZjyA?e=osceYD"}
        ]
    }
]

@app.route("/")
def home():
    return render_template("index.html", courses=courses)

if __name__ == "__main__":
    app.run(debug=True)