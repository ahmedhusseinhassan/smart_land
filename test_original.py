#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار endpoint الأصلي add_property
"""

import requests
import json

def test_original_endpoint():
    """اختبار endpoint الأصلي add_property"""
    
    test_data = {
        'property_title': 'عقار تجريبي - endpoint أصلي',
        'property_description': 'هذا عقار للاختبار endpoint الأصلي',
        'property_price_num': 600000,
        'property_area_num': 200,
        'property_location_1': 'الإسكندرية',
        'property_location_2': 'سيدي بشر'
    }

    print('🧪 اختبار endpoint الأصلي add_property...')
    try:
        response = requests.post(
            'http://localhost:8000/api/properties/add/',
            json=test_data,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        print(f'📊 كود الاستجابة: {response.status_code}')
        print(f'📄 الاستجابة: {response.text[:500]}...')
        
        if response.status_code == 200:
            print('✅ نجح الاختبار!')
            try:
                result = response.json()
                print(f'🎯 معرف العقار: {result.get("property_id")}')
                print(f'📍 المحافظة المحفوظة: {result.get("location_1")}')
                print(f'📍 المنطقة المحفوظة: {result.get("location_2")}')
            except:
                print('📄 الاستجابة ليست JSON صالح ولكن النجاح تم')
        else:
            print('❌ فشل الاختبار')
            
    except Exception as e:
        print(f'❌ خطأ في الاختبار: {e}')

if __name__ == "__main__":
    print("🚀 اختبار endpoint الأصلي...")
    print("=" * 50)
    test_original_endpoint()
    print("=" * 50)
    print("✅ انتهاء الاختبار") 