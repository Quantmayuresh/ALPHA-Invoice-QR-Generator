from qr_demo.qr_code import get_qr_code_print
import frappe
@frappe.whitelist()
def generate_qr_code(invoice_name): 

        cgst_rate = 0
        sgst_rate = 0
        igst_rate = 0
        cgst_amount = 0
        sgst_amount = 0
        igst_amount = 0
        doc=frappe.get_doc("Sales Invoice",invoice_name)
        if len(doc.get('items')) == 1 :
            cgst_rate = 0
            sgst_rate = 0
            igst_rate = 0
            cgst_amount = 0
            sgst_amount = 0
            igst_amount = 0
            doc=frappe.get_doc("Sales Invoice",invoice_name)
            if len(doc.get('items')) == 1 :
                for s in doc.items:
                        sgst_rate=s.sgst_rate
                        sgst_amount=s.sgst_amount
                        cgst_rate=s.cgst_rate
                        cgst_amount=s.cgst_amount
                        igst_rate=s.igst_rate
                        igst_amount=s.igst_amount

            for item in doc.items:
                part = frappe.get_value("Item", filters={'item_code': item.item_code}, fieldname='custom_part_number')

            new_date_format = doc.posting_date.strftime("%d.%m.%Y")
            no_data=0 
            qr_content =f'{doc.po_no if doc.po_no else 0},{10},{250096},IN,{new_date_format},{doc.name},{new_date_format},{doc.name},{part if part else 0 },{doc.total_qty},{item.uom},{str(doc.total)},{str(doc.net_total)},{cgst_amount},{sgst_amount},{igst_amount},{no_data},{cgst_rate},{sgst_rate},{igst_rate},{no_data},{doc.grand_total},{item.gst_hsn_code},{doc.company_gstin},{doc.currency}' 
            # frappe.throw(str(qr_content))
            return get_qr_code_print(str(qr_content))  
        else :
            frappe.msgprint("QR Not Generated")