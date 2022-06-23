#info:swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022

import pymysql


def main():
    no = int(input('要编辑的部门编号:'))
    loc = input('部门的新地址:')
    # 1.创建连接对象
    conn = pymysql.connect(host='123.56.242.173',
                           port=3306,
                           user='root',
                           password='123456',
                           database='hrs',
                           charset='utf8')
    try:
        # 2.获取游标对象
        with conn.cursor() as cursor:
            # 3.执行SQL得到结果
            result = cursor.execute('update tb_dept set dloc=%s where dno=%s', (loc, no))
            if result == 1:
                print('更新成功')
                # 4.操作成功执行提交
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        # 5.操作失败执行回滚
        conn.rollback()
    finally:
# 6.关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
