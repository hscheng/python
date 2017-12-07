select to_date(a.create_time) trans_date -- ��������
,b.trans_type trans_type -- ��������
,count(distint a.order_id) trans_cnt -- �����ܱ���
,count(distint case when a.status = 1 then a.order_id end) trans_cnt_succ -- ���׳ɹ�����
,sum(a.amount)/100 trans_amt -- �����ܽ��
,sum(case when a.status=1 then a.amount else 0 end)/100 trans_amt_succ -- ���׳ɹ����
from order_transaction a 
left join dim_trans b on a.channel_id = b.channel_id and b.dt=sysdate('yyyyMMdd',-1)
where a.dt = sysdate('yyyyMMdd',-1)
group by to_date(a.create_time)
,b.trans_type
;