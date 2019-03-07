while True:
    try:
        number= int(input("nhap so di ? \n"));
        print(18/number);
        break;
    except ValueError:
        print('khong co')
    except ZeroDivisionError:
        print('Không được nhập số 0')
    except :
        break;
    finally:
        print('xong')