from src.apis.trace_tx import trace_transaction_for_debug


from src.config import bsc_local_to_gcp_config
# 0x1a9c75236f8b31a6dc0c815d4d8c5b0e410355f6e7fd4e6b71ae60e75e4a0dac
# 0x45d1ef1925347a3d17d1dbed56d3797bdb9e130c3b23f9f4f622be8813900ccb
# 0x5ed2814fbfecad0027ea183dd94eb8dc3bd7e5741a730d2432548eec407eea29
# 0x905456f1e3cd5726f71fd97881b7b2f0649eaf65f5a71ee1f861b8eb202c21d4
tx_hash = "0x28faa81d399ac80ca666fe123aebd11eaaf77d2b2d5b3fee982aefd88d25ddde"

a = trace_transaction_for_debug(
    bsc_local_to_gcp_config.http_endpoint,
    tx_hash
)
print(a)
