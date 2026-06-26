# 1. 변경된 입력 데이터 정의 (헤더 1개당 라인 n개)
data = [
    ['Cust001', "SP001", "20260601", [
        ['RC00001', 100, '10%', 'DP001', 'CC001'],
        ['RC00002', 110, '10%', 'DP001', 'CC001']
    ]],
    ['Cust002', "SP002", "20260602", [
        ['RC00003', 200, '10%', 'DP002', 'CC002'],
        ['RC00004', 220, '10%', 'DP002', 'CC002']
    ]],
    ['Cust003', "SP003", "20260603", [
        ['RC00005', 300, '10%', 'DP003', 'CC003'],
        ['RC00006', 330, '10%', 'DP003', 'CC003']
    ]]
]

# 최종 마스터 리스트
saleTable_list = []
saleLine_list = []

# 2. 바깥쪽 반복문: 각 레코드(헤더 + 라인들)를 순회
for index, record in enumerate(data, 1):
    *header_part, lines_part = record
    
    print(f"\n================ [세트 {index}] ================")
    
    # [A] 헤더 데이터 추출 및 저장
    sale_table_row = {
        'Account': header_part[0],
        'SalesPoolId': header_part[1],
        'DeliveryDate': header_part[2]
    }
    saleTable_list.append(sale_table_row)
    
    # 헤더 한 줄 출력
    print(f"[saleTable 출력] {sale_table_row}")
    print("-" * 50)
    
    # [B] 안쪽 반복문: 현재 헤더에 속한 여러 개의 라인을 순회
    for line in lines_part:
        sale_line_row = {
            'Account': header_part[0],  # 외래키(FK) 역할을 위해 헤더의 Account 추가
            'ItemId': line[0],
            'Qty': line[1],
            'ItemTaxCode': line[2],
            'FinDimDept': line[3],
            'FinDimCostCenter': line[4]
        }
        saleLine_list.append(sale_line_row)
        
        # 라인 출력 (여기서 각 세트당 두 줄씩 출력됩니다)
        print(f"  └─ [saleLine 출력] {sale_line_row}")

print("\n==============================================")
print("최종 변환 작업이 완료되었습니다.")