#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار سريع للتحقق من عمل endpoints الجديدة
"""

import requests
import json

def test_no_validation_endpoint():
    """اختبار endpoint الجديد add-property-no-validation"""
    
    test_data = {
        'property_title': 'عقار تجريبي - أي محافظة',
        'property_description': 'هذا عقار للاختبار مع محافظة ومنطقة جديدة تماماً',
        'property_price_num': 500000,
        'property_area_num': 150,
        'property_location_1': 'محافظة جديدة لا توجد في قاعدة البيانات',
        'property_location_2': 'منطقة جديدة تماماً'
    }

    print('🧪 اختبار endpoint الجديد add-property-no-validation...')
    try:
        response = requests.post(
            'http://localhost:8000/api/properties/add-no-validation/',
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

def test_simple_endpoint():
    """اختبار endpoint البسيط للمقارنة"""
    
    test_data = {
        'property_title': 'عقار تجريبي بسيط',
        'property_description': 'وصف بسيط',
        'property_price_num': 100000,
        'property_area_num': 100
    }

    print('\n🧪 اختبار endpoint البسيط test-add-property-simple...')
    try:
        response = requests.post(
            'http://localhost:8000/api/test/add-property-simple/',
            json=test_data,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        print(f'📊 كود الاستجابة: {response.status_code}')
        print(f'📄 الاستجابة: {response.text[:500]}...')
        
        if response.status_code == 200:
            print('✅ نجح الاختبار!')
        else:
            print('❌ فشل الاختبار')
            
    except Exception as e:
        print(f'❌ خطأ في الاختبار: {e}')

if __name__ == "__main__":
    print("🚀 بدء الاختبارات السريعة...")
    print("=" * 50)
    
    test_no_validation_endpoint()
    test_simple_endpoint()
    
    print("\n" + "=" * 50)
    print("✅ انتهاء الاختبارات") 