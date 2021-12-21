from electrum.bitcoin import script_to_p2wsh
from electrum.crypto import hmac_oneshot
import hashlib
import hmac
import time
from backports.pbkdf2 import pbkdf2_hmac
import pbkdf2_ctypes

x = "new seed"
salt = bytes.fromhex('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
time_z = time.time()
key = hashlib.pbkdf2_hmac('sha512', "514d82030709603de50a22d14371f56c872056036d849fa6c82a07149ee443bd915fb56489a3db903a216ec54bee216d7cf063e4ce6d1d07b02024710ac60c80742079681c8a359cf851605f20f439890823ed539055599e2e233dc0e6175aaaeba04946150107a8080e4dbe99ea16a5dee70765a463b543ec59796625658a8765b0f682db99ef2254011143c09849157f67111fb743d91b655e42b48f09d58bb8d0656024396aa8da207efe182661ac1e92e961596e9ddf44b6148a9bdd4f1c70dc87afc8d8199820a5930f143062c7d828dd5a8bd551b78a014f578e85044e8f3914e56267df8b7e26d64bf39f11ca9da6db44564a8c5968955586c1075d69e174d08426b29877d92160679da138c51153f9547297d805ab1c4a3e0499e3ae1c0cdacc2a268306bd0811b3264cb11046a801be23790da26669b41b8882f8b14a2c11187b55cd50dbdc260bb587d9972af52ac923f68ba2c86fa1b43598e051182aced14fa95683c1f3908aa0e9898ce9087ccbc84fc64696a1441255c9c578eed9c83a415e0358a51e788849cb6d810e16feba70388a4b3ce63538b808154f1815dad328e3a265b3835357e4a44874210b8c1e818cb5871eadca8474df7a14d1d702f1b017f2d6235bcc4383270b096d9d51412d5efc1a1149d01217c700dd5b810eef3f245e4628988eed1c4d745a79696751ee84166c9f7c6aa9fd725700cd2d1134b17f8f69b91ab6a6b1e44c54697cc7b7cbf474cd7c2ac9d804368554a53dab7d5d3cb0353e82048338501b15c26b95d4b8a1a29884ad219604ecd33622010706fa25674b2961bbd181d5b9728f982f5dd37695d1f56dc0fd41e867f46e830eac38a3c4210ac7994a85e3c1ec899651457a761fa3024a083922a485bca16b8348ef98b2feeec7ad6e80b3caf519fb1aa34c80e514c49d92580eb0fa329af7279e7eda925afb5ede0a737641c3bd00fa59e56c22be6a0359a704bc5ca645d2ddd149b8a0136b75987c782259e67407c56b797bcb88dd5f4fc6449bb5532084b1f1999be73f92e543163e59a875107cba4710f092a66d7672e75996f0b73055009395d059ca0f99d90b8abe5b47837608aceaa9c4293630f2c7d7759e4053fe05a60f173c888ee3f981e6ed9ac2bcb5b6d8be5c12fc86125be70f125c32691e1ab48c8104d820307092b9434906924ba57903d1695195b920511898ad024131c55911507b511350dab89de844f057bb1a4922a0561d0f4b9556f38e52ab90403cb122a66f6c487ef21a044772390095daeae236d9598434542d132eb52aa35120ac44aa291c11849534823abbaa2f7578491a8fa591a2493d606124991e967b90d8e81b23103d01ce54ef8792d133b85c8d2ff44418e65a902938d9b2dd0a47244547c86b47bca9cc4ca9a981118941fa".encode(),
                          salt, iterations=500000, dklen=48)
print(time.time()-time_z)

time_z = time.time()
salt = bytes.fromhex('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = "514d82030709603de50a22d14371f56c872056036d849fa6c82a07149ee443bd915fb56489a3db903a216ec54bee216d7cf063e4ce6d1d07b02024710ac60c80742079681c8a359cf851605f20f439890823ed539055599e2e233dc0e6175aaaeba04946150107a8080e4dbe99ea16a5dee70765a463b543ec59796625658a8765b0f682db99ef2254011143c09849157f67111fb743d91b655e42b48f09d58bb8d0656024396aa8da207efe182661ac1e92e961596e9ddf44b6148a9bdd4f1c70dc87afc8d8199820a5930f143062c7d828dd5a8bd551b78a014f578e85044e8f3914e56267df8b7e26d64bf39f11ca9da6db44564a8c5968955586c1075d69e174d08426b29877d92160679da138c51153f9547297d805ab1c4a3e0499e3ae1c0cdacc2a268306bd0811b3264cb11046a801be23790da26669b41b8882f8b14a2c11187b55cd50dbdc260bb587d9972af52ac923f68ba2c86fa1b43598e051182aced14fa95683c1f3908aa0e9898ce9087ccbc84fc64696a1441255c9c578eed9c83a415e0358a51e788849cb6d810e16feba70388a4b3ce63538b808154f1815dad328e3a265b3835357e4a44874210b8c1e818cb5871eadca8474df7a14d1d702f1b017f2d6235bcc4383270b096d9d51412d5efc1a1149d01217c700dd5b810eef3f245e4628988eed1c4d745a79696751ee84166c9f7c6aa9fd725700cd2d1134b17f8f69b91ab6a6b1e44c54697cc7b7cbf474cd7c2ac9d804368554a53dab7d5d3cb0353e82048338501b15c26b95d4b8a1a29884ad219604ecd33622010706fa25674b2961bbd181d5b9728f982f5dd37695d1f56dc0fd41e867f46e830eac38a3c4210ac7994a85e3c1ec899651457a761fa3024a083922a485bca16b8348ef98b2feeec7ad6e80b3caf519fb1aa34c80e514c49d92580eb0fa329af7279e7eda925afb5ede0a737641c3bd00fa59e56c22be6a0359a704bc5ca645d2ddd149b8a0136b75987c782259e67407c56b797bcb88dd5f4fc6449bb5532084b1f1999be73f92e543163e59a875107cba4710f092a66d7672e75996f0b73055009395d059ca0f99d90b8abe5b47837608aceaa9c4293630f2c7d7759e4053fe05a60f173c888ee3f981e6ed9ac2bcb5b6d8be5c12fc86125be70f125c32691e1ab48c8104d820307092b9434906924ba57903d1695195b920511898ad024131c55911507b511350dab89de844f057bb1a4922a0561d0f4b9556f38e52ab90403cb122a66f6c487ef21a044772390095daeae236d9598434542d132eb52aa35120ac44aa291c11849534823abbaa2f7578491a8fa591a2493d606124991e967b90d8e81b23103d01ce54ef8792d133b85c8d2ff44418e65a902938d9b2dd0a47244547c86b47bca9cc4ca9a981118941fa".encode("utf8")
key = pbkdf2_hmac("SHA512", passwd, salt, 500000, 48)
print(time.time()-time_z)

time_z = time.time()
salt = bytes.fromhex('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = "514d82030709603de50a22d14371f56c872056036d849fa6c82a07149ee443bd915fb56489a3db903a216ec54bee216d7cf063e4ce6d1d07b02024710ac60c80742079681c8a359cf851605f20f439890823ed539055599e2e233dc0e6175aaaeba04946150107a8080e4dbe99ea16a5dee70765a463b543ec59796625658a8765b0f682db99ef2254011143c09849157f67111fb743d91b655e42b48f09d58bb8d0656024396aa8da207efe182661ac1e92e961596e9ddf44b6148a9bdd4f1c70dc87afc8d8199820a5930f143062c7d828dd5a8bd551b78a014f578e85044e8f3914e56267df8b7e26d64bf39f11ca9da6db44564a8c5968955586c1075d69e174d08426b29877d92160679da138c51153f9547297d805ab1c4a3e0499e3ae1c0cdacc2a268306bd0811b3264cb11046a801be23790da26669b41b8882f8b14a2c11187b55cd50dbdc260bb587d9972af52ac923f68ba2c86fa1b43598e051182aced14fa95683c1f3908aa0e9898ce9087ccbc84fc64696a1441255c9c578eed9c83a415e0358a51e788849cb6d810e16feba70388a4b3ce63538b808154f1815dad328e3a265b3835357e4a44874210b8c1e818cb5871eadca8474df7a14d1d702f1b017f2d6235bcc4383270b096d9d51412d5efc1a1149d01217c700dd5b810eef3f245e4628988eed1c4d745a79696751ee84166c9f7c6aa9fd725700cd2d1134b17f8f69b91ab6a6b1e44c54697cc7b7cbf474cd7c2ac9d804368554a53dab7d5d3cb0353e82048338501b15c26b95d4b8a1a29884ad219604ecd33622010706fa25674b2961bbd181d5b9728f982f5dd37695d1f56dc0fd41e867f46e830eac38a3c4210ac7994a85e3c1ec899651457a761fa3024a083922a485bca16b8348ef98b2feeec7ad6e80b3caf519fb1aa34c80e514c49d92580eb0fa329af7279e7eda925afb5ede0a737641c3bd00fa59e56c22be6a0359a704bc5ca645d2ddd149b8a0136b75987c782259e67407c56b797bcb88dd5f4fc6449bb5532084b1f1999be73f92e543163e59a875107cba4710f092a66d7672e75996f0b73055009395d059ca0f99d90b8abe5b47837608aceaa9c4293630f2c7d7759e4053fe05a60f173c888ee3f981e6ed9ac2bcb5b6d8be5c12fc86125be70f125c32691e1ab48c8104d820307092b9434906924ba57903d1695195b920511898ad024131c55911507b511350dab89de844f057bb1a4922a0561d0f4b9556f38e52ab90403cb122a66f6c487ef21a044772390095daeae236d9598434542d132eb52aa35120ac44aa291c11849534823abbaa2f7578491a8fa591a2493d606124991e967b90d8e81b23103d01ce54ef8792d133b85c8d2ff44418e65a902938d9b2dd0a47244547c86b47bca9cc4ca9a981118941fa".encode("utf8")
key = pbkdf2_ctypes.pbkdf2_bin(passwd, salt, 500000, 48, hashlib.sha512)
print(time.time()-time_z)

