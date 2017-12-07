select to_date(a.create_time) trans_date -- 订单日期
,b.trans_type trans_type -- 交易类型
,count(distint a.order_id) trans_cnt -- 交易总笔数
,count(distint case when a.status = 1 then a.order_id end) trans_cnt_succ -- 交易成功笔数
,sum(a.amount)/100 trans_amt -- 交易总金额
,sum(case when a.status=1 then a.amount else 0 end)/100 trans_amt_succ -- 交易成功金额
from order_transaction a 
left join dim_trans b on a.channel_id = b.channel_id and b.dt=sysdate('yyyyMMdd',-1)
where a.dt = sysdate('yyyyMMdd',-1)
group by to_date(a.create_time)
,b.trans_type
;