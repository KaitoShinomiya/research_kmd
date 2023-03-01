SMAPLE_DATA_JSON = {
    "DigitalReceipt": {
        "@@MajorVersion": "3",
        "Transaction": [
            {
                "BusinessUnit": [
                    {
                        "UnitID": {
                            "@@Name": "塩尻駅前店",  # str,uncover,must be fixed
                            "#value": "WWWWXXXX"   # uuid,uncover,must be fixed
                        }, "Address": {
                            # str,uncover,must be fixed
                            "AddressLine": [{"#value": "広岡-123"}],
                            "City": "塩尻市",
                            "PostalCode": "399-yyz"
                        },
                        "Telephone": {
                            # int, uncover,must be fixed
                            "AreaCode": "0263",
                            "LocalNumber": ["yyzzzz"]
                        }
                    }
                ],
                "Logo": {
                    # type(PDF,JPG,PNG,SVG ans so on),uncover,necessary
                    # depeding on the situation
                    "@@LogoFormat": "PDF",
                    # str uncover,necessary depeding on the situation
                    "FileName": "www.myreceipts.com/123456789999"
                },
                "SequenceNumber": 50,  # uuid or int,uncover
                "OperatorID": [
                    {
                        "@@OperatorName": "太田 ザーキー",  # str cover
                        "#value": "78956"  # int or uuid, cover
                    }
                ],
                # datetime,must be fixed,uncover
                "ReceiptDateTime": {"#value": "2006-05-04T18:13:51.0Z"},
                "RetailTransaction": [
                    {
                        "LineItem": [
                            {
                                "Sale": {
                                    "ItemID": [
                                        {
                                            "@@Name": "ノンアルコールビール",  # str
                                            # int(バーコードnum)
                                            "#value": "1022585345677"
                                        }
                                    ],
                                    # int,uncover
                                    "ExtendedAmount": {"#value": 720},
                                    # int, uncover
                                    "Quantity": [{"#value": 6}],
                                    # marchandise type(str),uncover
                                    "cotegory": ["sampple"],
                                    # purpose_type(str),uncover
                                    "purpose":"sample"
                                },
                                "SequenceNumber": [1]
                            },
                            {
                                "Tender": {
                                    "@@TenderType": "CreditDebit",  # payment_type,uncover,must be fixed
                                    # int,uncover,must be fixed
                                    "Amount": {"#value": 5551},
                                    "CreditDebit": [
                                        {
                                            # credit_card_type(str),uncover,must
                                            # be fixed
                                            "@@TypeCode": "Visa",
                                            # credit_card_type(str),cover,must
                                            # be fixed
                                            "PrimaryAccountNumber": {"#value": "*********yyyyzz"}
                                        }
                                    ]
                                },
                                "SequenceNumber": [5]
                            }
                        ],
                        "Total": [
                            {
                                "@@TotalType": "TransactionGrossAmount",
                                "#value": 5140  # int, uncover, must be fixed
                            },
                            {
                                "@@TotalType": "TransactionNetAmount",
                                "#value": 5140  # int, uncover,　must be fixed
                            },
                            {
                                "@@TotalType": "TransactionGrandAmount",
                                "#value": 5551
                            },
                            {
                                "@@TotalType": "TransactionTaxAmount",
                                "#value": 411  # int,uncover,must be fixed
                            }
                        ],
                        "LoyaltyAccount": [
                            {
                                # userid(hex),uncover,must be fixed
                                "CustomerID": "yyy896557",
                                "LoyaltyAccount": {
                                    "ExpirationDate": "2020-08-30",  # datetime,uncover,must be fixed
                                    "Points": [
                                        {
                                            "@@Type": "PreviousPoints",  # int uncover
                                            "#value": 600
                                        },
                                        {
                                            "@@Type": "Redeemed",  # int uncover
                                            "#value": 0
                                        },
                                        {
                                            "@@Type": "PointsEarned",  # int uncover
                                            "#value": 514
                                        },
                                        {
                                            "@@Type": "Balance",  # int uncover
                                            "#value": 1114
                                        }
                                    ],
                                    "PointsExpiration": [
                                        {

                                            # int uncover
                                            "ToBeExpiredPoints": {"#value": 600},
                                            "PointsExpirationDate": "2016-03-20"  # int uncover
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
