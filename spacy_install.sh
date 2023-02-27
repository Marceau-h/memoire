$1 -m pip install -U pip setuptools wheel
$1 -m pip install -U 'spacy[transformers,lookups]'

$1 -m spacy download en_core_web_sm
$1 -m spacy download en_core_web_md
$1 -m spacy download en_core_web_lg
$1 -m spacy download en_core_web_trf

$1 -m spacy download fr_core_news_sm
$1 -m spacy download fr_core_news_md
$1 -m spacy download fr_core_news_lg
$1 -m spacy download fr_core_news_lg

$1 -m spacy download ca_core_news_sm
$1 -m spacy download zh_core_web_sm
$1 -m spacy download hr_core_news_sm
$1 -m spacy download da_core_news_sm
$1 -m spacy download nl_core_news_sm
$1 -m spacy download fi_core_news_sm
$1 -m spacy download de_core_news_sm
$1 -m spacy download it_core_news_sm
$1 -m spacy download ja_core_news_sm
$1 -m spacy download ko_core_news_sm
$1 -m spacy download lt_core_news_sm
$1 -m spacy download mk_core_news_sm
$1 -m spacy download nb_core_news_sm
$1 -m spacy download pl_core_news_sm
$1 -m spacy download pt_core_news_sm
$1 -m spacy download ro_core_news_sm
$1 -m spacy download ru_core_news_sm
$1 -m spacy download es_core_news_sm
$1 -m spacy download sv_core_news_sm
$1 -m spacy download uk_core_news_sm