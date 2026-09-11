from hdbcli import dbapi
import pandas as pd
import redshift_connector
import awswrangler as wr

hana_conn = dbapi.connect(
    address='10.46.0.49',
        port=30615,
        user='RNB4003',
        password='Manaswini@19933797@@',
        encrypt=True,                 
        sslValidateCertificate=False    
)

print('hana connection successful')

red_conn = redshift_connector.connect(
    host='redshift-vcpe-cu-cluster-dev-endpoint-mkdlzvzupzunz9m2vsvy.czngkhaq6arh.us-east-1.redshift.amazonaws.com',
    database='analytics_d',
    port=5439,
    user='ajs4014',
    password='Changed@0986'           
)

cursor = hana_conn.cursor()
query = """SELECT
    OHREQUID      AS OHREQUID,
    DATAPAKID     AS DATAPAKID,
    RECORD        AS RECORD,
    AC_DOC_NO     AS "Document Number",
    BBP_INV_ID    AS "PO Invoice Number",
    BBP_POITEM    AS "BBP_POITEM",
    BBP_PO_ID     AS "Purchase Order No",
    BLINE_DATE    AS "Base Date",
    CLEAR_DATE    AS "Clearing Date",
    CMMT_ITEM     AS "Commitment Item",
    COMP_CODE     AS "Company Code",
    COORDER       AS "Internal Order",
    COSTCENTER    AS "Cost Center",
    COUNTRY       AS "COUNTRY",
    CO_AREA       AS "Controlling Area",
    CREATEDON     AS "Created On",
    CREDITOR      AS "Vendor",
    DCINDIC       AS "Debit Credit",
    DOC_DATE      AS "Document Date",
    DOC_HD_TXT    AS "Document Header Text",
    FG_ITEXT      AS "Item Text",
    FISCPER       AS "Fiscal Period",
    FISCPER3      AS "Posting Period",
    FISCVARNT     AS "Fiscal Year Variant",
    FISCYEAR      AS "Fiscal Year",
    FI_DOCSTAT    AS "Item Status",
    FM_AREA       AS "FM Area",
    FUNDS_CTR     AS "Funds Center",
    GM_SPNPG      AS "GM_SPNPG",
    INFOPROV      AS "INFOPROV",
    ITEM_NUM      AS "Item",
    NETDUEDATE    AS "Net Due Date",
    PMNTTRMS      AS "Terms of Payment",
    PMTMTHSUPL    AS "PMTMTHSUPL",
    PROD_CATEG    AS "PROD_CATEG",
    PROD_TYPE     AS "PROD_TYPE",
    PSTNG_DATE    AS "Posting Date",
    PURCH_ORG     AS "Purchasing Org",
    PYMT_METH     AS "Payment Method",
    REFDOC_ITM    AS "Previous Doc Item",
    REF_DOC_NO    AS "Reference Doc",
    REF_TRXN      AS "Reference Transaction",
    USERNAME      AS "User Name",
    TOTAL         AS "TOTAL",
    CKYTOTAL      AS "CKYTOTAL",
    POINVGR       AS "POINVGR",
    CKYPOINVGR    AS "CKYPOINVGR",
    POINVNY       AS "POINVNY",
    CKYPOINVNY    AS "CKYPOINVNY",
    POGRQA        AS "POGRQA",
    CKYPOGRQ      AS "CKYPOGRQ",
    NONPOSPND     AS "Non PO Spend",
    CKYNONPOS     AS "CKYNONPOS",
    PCARD         AS "Pcard",
    CKYPCARD      AS "CKYPCARD",
    PAYMREQ       AS "Payment Request",
    CKYPAYREQ     AS "CKYPAYREQ",
    TRAVLEXP      AS "Travel Expense",
    CKYTRVEXP     AS "CKYTRVEXP",
    TRAVLEXPNY    AS "TRAVLEXPNY",
    CKYTRAEXNY    AS "CKYTRAEXNY",
    TRVLEXPQ      AS "TRVLEXPQ",
    CKYTREXPQ     AS "CKYTREXPQ",
    MANINCREC     AS "MANINCREC",
    CKYMANINC     AS "CKYMANINC",
    OTHERS        AS "OTHERS",
    CKYOTHERS     AS "CKYOTHERS",
    PCARDL3       AS "PCARDL3",
    CKYPCARDL3    AS "CKYPCARDL3",
    INVAMT        AS "Invoice Amount",
    CKYINVAMT     AS "CKYINVAMT",
    AGDCPOS       AS "AGDCPOS",
    AGDCOPE       AS "AGDCOPE",
    AGDCDUE       AS "AGDCDUE",
    TAXAMT        AS "Tax Amount",
    CKYTAXAMT     AS "CKYTAXAMT",
    GROSAMTO      AS "Gross Amount",
    CKYGRSAMTO    AS "CKYGRSAMTO",
    AMTFMCUR        AS "AMTFMCUR",
    CKYAMTFM        AS "CKYAMTFM",
    "/BIC/ZACCT"    AS "Fund SP",
    "/BIC/ZADATE"   AS "BIC ZADATE",
    "/BIC/ZAGCATOI" AS "BIC ZAGCATOI",
    "/BIC/ZCHEQUE"  AS "Check Number",
    "/BIC/ZCLR_DOC" AS "Clearing Document",
    "/BIC/ZCOUNTER2" AS "BIC ZCOUNTER2",
    "/BIC/ZDEPART"  AS "Department",
    "/BIC/ZFI_DESC" AS "BIC ZFI_DESC",
    "/BIC/ZLEGDAT"  AS "Legacy Date",
    "/BIC/ZMERCHNM" AS "PCARD Merchant Name",
    "/BIC/ZPTCATDD" AS "BIC ZPTCATDD",
    "/BIC/ZPTCATPD" AS "BIC ZPTCATPD",
    "/BIC/ZTRANAME" AS "Traveller Name",
    "/BIC/ZTRVTYPE" AS "Traveller Type",
    "/BIC/ZUSERNM"  AS "PCARD Owner",
    "/BIC/ZVISA_MC" AS "Merchant Category",
    "/BIC/ZXBLNR"   AS "BIC ZXBLNR",
    AC_DOC_TYP      AS "Document type",
    PMNT_BLOCK      AS "Payment block",
    "/BIC/ZCTEBUPC" AS "BIC ZCTEBUPC",
    "/BIC/ZCTEVEND" AS "CTE Vendor",
    "/BIC/ZPYMTTYP" AS "Payment Type",
    "/BIC/ZPCARDIND" AS "BIC ZPCARDIND",
    ACCT_FUNDCTR    AS "ACCT_FUNDCTR",
    ACCT_FLAG       AS "ACCT_FLAG",
    CHEQUE_ENCDT    AS "CHEQUE_ENCDT",
    CHEQUE_VOIDR    AS "CHEQUE_VOIDR",
    CHEQUE_VOIDCKD  AS "CHEQUE_VOIDCKD",
    CLRDOC_CARTNO   AS "CLRDOC_CARTNO",
    CLRDOC_SDATE    AS "CLRDOC_SDATE",
    CREDTOR_ALTPAYE AS "CREDTOR_ALTPAYE",
    ZACCT_TXT       AS "Fund SP Text",
    CMMT_ITEM_TXT   AS "CMMT_ITEM_TXT",
    PYMTMETH_TXT    AS "PYMTMETH_TXT",
    CREDITOR_TXT    AS "CREDITOR_TXT",
    AC_DOC_TYP_TXT  AS "AC_DOC_TYP_TXT",
    PMNT_BLOCK_TXT  AS "PMNT_BLOCK_TXT",
    ZUSERNM_TXT     AS "ZUSERNM_TXT",
    ZPCARDIND_TXT   AS "ZPCARDIND_TXT",
    PMNTTRMS_TXT    AS "PMNTTRMS_TXT",
    PMTMTHSUPL_TXT  AS "PMTMTHSUPL_TXT",
    FI_DOCSTAT_TXT  AS "FI_DOCSTAT_TXT",
    COORDER_TXT     AS "COORDER_TXT",
    USERNAME_TXT    AS "USERNAME_TXT",
    ZACCT_KEY       AS "ZACCT_KEY",
    ZACCT_NUM       AS "ZACCT_NUM",
    ZACCT_CONCAT    AS "Fund SP_CON"
from SAPBWD."/BIC/OHZAP_OH2" """

df_hana = pd.read_sql(query, hana_conn)

num_cols = len(df_hana.columns)

chunks = max(1, 30000 // num_cols)

print(f"Columns: {num_cols} | Safe Row Chunksize: {chunks}")

hana_conn.close()
# print(list(df_hana.columns))

print(f'start_time: {pd.Timestamp.now()}')
wr.redshift.to_sql(
    df=df_hana,
    con=red_conn,
    schema='wcm_fi',
    table='ap_details_history',
    mode="overwrite", 
    index=False,
    chunksize=chunks    
)
red_conn.commit()

print('data written to redshift successfully')
print(f'end_time: {pd.Timestamp.now()}')

red_conn.close()
