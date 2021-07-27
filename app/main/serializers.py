
def sql_result_serializer(query_result,row_headers):
    json_data = []
    for result in query_result:
        json_data.append(dict(zip(row_headers, result)))
    return json_data
