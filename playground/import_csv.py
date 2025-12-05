import pandas as pd
from playground.models import ThirdRail

file_path = r"C:\Users\orange\Desktop\store\thirdrail.csv"
print("📦 Starting import from:", file_path)

# Try multiple encodings
encodings = ['utf-8-sig', 'latin-1', 'windows-1252']
df = None
for enc in encodings:
    try:
        df = pd.read_csv(file_path, encoding=enc)
        print(f"✅ File successfully read using {enc} encoding")
        break
    except Exception as e:
        print(f"⚠️ Failed with encoding {enc}: {e}")

if df is None:
    print("❌ Could not read file with any encoding.")
    exit()

# Normalize column names
df.columns = [col.strip().lower().replace(" ", "_").replace("/", "_").replace("#", "").replace(".", "") for col in df.columns]
print("🧩 Columns found:", list(df.columns))

# Map CSV columns to model fields
col_map = {
    's_no': 'sr_no',
    'product_id': 'product_id',
    'register_pg_no': 'register_page_no',
    '': 'tools_and_spares',   # your empty column
    'cabinet_': 'cabinet_no',
    'rack': 'rack_no',
    'product_description': 'product_description',
    'product_desc_ription': 'product_description',  # messy header
    'product_category': 'product_category',
    'store_stock': 'store_stock',
    'column4': 'column4',
    'column3': 'column3',
    'column2': 'column2',
    'column1': 'column1',
    'remarks': 'remarks'
}

# Delete old records
ThirdRail.objects.all().delete()
print("🗑️ Old records deleted.")

# Import new records
count = 0
for _, row in df.iterrows():
    # Handle sr_no properly
    sr_no_value = row.get('s_no', row.get('s_no.', None))
    if pd.notna(sr_no_value) and sr_no_value != '':
        sr_no_value = str(int(sr_no_value))  # 1.0 -> "1"
    else:
        sr_no_value = ''

    ThirdRail.objects.create(
        sr_no=sr_no_value,
        product_id=row.get('product_id', ''),
        register_page_no=row.get('register_pg_no', ''),
        tools_and_spares=row.get('', ''),
        cabinet_no=row.get('cabinet_', ''),
        rack_no=row.get('rack', ''),
        product_description=row.get('product_description', row.get('product_desc_ription', '')),
        product_category=row.get('product_category', ''),
        store_stock=row.get('store_stock', ''),
        column4=row.get('column4', ''),
        column3=row.get('column3', ''),
        column2=row.get('column2', ''),
        column1=row.get('column1', ''),
        remarks=row.get('remarks', '')
    )
    count += 1

print(f"✅ Successfully imported {count} items into thirdrail table!")
