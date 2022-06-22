from inventorydata import InventoryData
    
    def alllist():    
        rows = InventoryData.load_data(url)
        data = pd.DataFrame(rows)
        #index_title = "All"
        data['Item'] = data['Item'].str.lower()
        data = data.sort_values(by=['Item'])
        data['Item'] = data['Item'].str.title()
        #data.index = data.index.factorize()[0] + 1
        return data