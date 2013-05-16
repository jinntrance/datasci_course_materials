select f1.docid,f2.docid,sum(f1.count*f2.count) s
from (SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count) f1,frequency f2
where f1.term=f2.term
group by f1.docid,f2.docid
order by s;

