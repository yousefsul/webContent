import json
from connectMongoDB import ConnectMongoDB
from web_parser.page_parser import PageParser

if __name__ == '__main__':
    claim_status_codes_url = "https://x12.org/codes/claim-status-codes"

    codes_page_url = "https://x12.org/codes/claim-status-codes"
    web_parser = PageParser(url=codes_page_url,
                            content_request_tag='tr',
                            content_request_sub_tag='td',
                            content_request_css_tag='codelist',
                            main_tag='table',
                            sub_tag='tbody'
                            )
    connection = ConnectMongoDB()

    status_codes = web_parser.get_status_codes()
    # connection.connect_claim_status_codes_collection_collection()
    # connection.insert_to_claim_status_codes_collection(status_codes)
    # print(json.dumps(status_codes,indent=4))

    claim_status_category_codes_url = "https://x12.org/codes/claim-status-category-codes"
    web_parser = PageParser(url=claim_status_category_codes_url,
                            content_request_tag='tr',
                            content_request_sub_tag='td',
                            content_request_css_tag='codelist',
                            main_tag='table',
                            sub_tag='tbody'
                            )
    status_codes = web_parser.get_status_codes()
    # connection.connect_to_claim_status_category_codes_collection()
    # connection.insert_to_claim_status_category_codes_collection_collection(status_codes)
    # print(json.dumps(status_codes, indent=4))

# outboud 837 270 276

# 837 ack-> ta1 999 277ca + response /2-3 weeks 835

# 270 ack-> ta1 999 + response 271 /hours

# 276 ack-> ta1 999 + response 277 /hours

# code_list__code-list-table


# https://x12.org/codes/claim-status-category-codes

# https://x12.org/codes/claim-status-codes
