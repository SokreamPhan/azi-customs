# -*- coding: utf-8 -*-

{
    "name": "Purchase Extension",
    "author": "A2A Digital",
    "version": "8.0.1.0.0",
    "category": "Purchase Management",
    "depends": [
        "purchase", "purchase_requisition", "purchase_request", "stock",
    ],
    "data": [
        "views/stock.xml",
        "views/report_stockpicking.xml",
        "views/report_purchaserequests.xml",
        "views/purchase_order_view.xml",
        "views/report_purchaserequisitions.xml",
        'views/report_purchaseorder.xml',
    ],
    "license": 'AGPL-3',
    "installable": True
}
