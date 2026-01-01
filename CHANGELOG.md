# Changelog

## 1.5.0 (2026-01-01)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/mpatankar/met-museum/compare/v1.4.0...v1.5.0)

### Features

* **api:** add MCP server support ([#33](https://github.com/mpatankar/met-museum/issues/33)) ([792e542](https://github.com/mpatankar/met-museum/commit/792e542b7dc1cff422f7faab7ff404266f89dd4c))
* **api:** manual updates ([97371ed](https://github.com/mpatankar/met-museum/commit/97371ede05912fd8a069df36690104d8ac41aea7))
* **api:** manual updates ([0e3def8](https://github.com/mpatankar/met-museum/commit/0e3def8a220413ef283ad205f307fa6e754ed5a2))
* **api:** manual updates ([0204572](https://github.com/mpatankar/met-museum/commit/020457232095d9f35c01fb745ee90f16c30d4bd4))
* **api:** manual updates ([3789a26](https://github.com/mpatankar/met-museum/commit/3789a268a3a61696278c2eb3cedcb7df1cf405ae))
* **api:** manual updates ([5f60c08](https://github.com/mpatankar/met-museum/commit/5f60c08b84d90d5d94ebea58c3b40d3ec302de65))
* **api:** manual updates ([f3b67fb](https://github.com/mpatankar/met-museum/commit/f3b67fb982cd9e4034161c3cc963787771a792cd))
* **api:** removed fast_api path ([57be10f](https://github.com/mpatankar/met-museum/commit/57be10f260a63fc32ceab49f038d06b630c0c958))
* **client:** make the title param required ([#25](https://github.com/mpatankar/met-museum/issues/25)) ([395dd27](https://github.com/mpatankar/met-museum/commit/395dd27e595cf7cce1c3d156ad263eb3f407523b))


### Bug Fixes

* **ci:** ensure pip is always available ([#31](https://github.com/mpatankar/met-museum/issues/31)) ([8528f3c](https://github.com/mpatankar/met-museum/commit/8528f3cf3e48b356ac654ff83073c5463ab156d9))
* **ci:** remove publishing patch ([#32](https://github.com/mpatankar/met-museum/issues/32)) ([5d9f5cd](https://github.com/mpatankar/met-museum/commit/5d9f5cd11846801f7600e005d3381bc22a0644c9))
* **package:** support direct resource imports ([e192feb](https://github.com/mpatankar/met-museum/commit/e192feb39e2ed30641c1e2df8f3beb3192070a81))
* **perf:** optimize some hot paths ([fd38b3c](https://github.com/mpatankar/met-museum/commit/fd38b3c8ed374401aba72155dbd93b45ec0edb47))
* **perf:** skip traversing types for NotGiven values ([e873181](https://github.com/mpatankar/met-museum/commit/e87318175ab7a5195cf26fd9d5ab2043d96598ae))
* **pydantic v1:** more robust ModelField.annotation check ([c8b3ade](https://github.com/mpatankar/met-museum/commit/c8b3ade8c1fa1267767d4d84084508a44b888777))
* **types:** handle more discriminated union shapes ([#30](https://github.com/mpatankar/met-museum/issues/30)) ([ee31779](https://github.com/mpatankar/met-museum/commit/ee31779534655f33d51fe740961e0d18a4cf1bef))


### Chores

* broadly detect json family of content-type headers ([f150d83](https://github.com/mpatankar/met-museum/commit/f150d83707dff515e2c3388cacecfe25fb84c0db))
* **ci:** add timeout thresholds for CI jobs ([bb82083](https://github.com/mpatankar/met-museum/commit/bb82083722c65332d38dc3ed8779bef8f3e0d192))
* **ci:** only use depot for staging repos ([a14d0b0](https://github.com/mpatankar/met-museum/commit/a14d0b0aea9e605eedcd80fd8dd5617dc12520d6))
* **client:** minor internal fixes ([7ddc090](https://github.com/mpatankar/met-museum/commit/7ddc09066616d226036c6d4e4e0ac15c119092f1))
* **internal:** avoid errors for isinstance checks on proxies ([3d2f5ca](https://github.com/mpatankar/met-museum/commit/3d2f5ca02fb033b50b54479c5f0c9eb37e5c932d))
* **internal:** base client updates ([d94120a](https://github.com/mpatankar/met-museum/commit/d94120a483fdf07be22cd9f0f34e765c420027f7))
* **internal:** bump pyright version ([aa0a40c](https://github.com/mpatankar/met-museum/commit/aa0a40c55fee7f321e169263be9e33ed495bb9c1))
* **internal:** bump rye to 0.44.0 ([#28](https://github.com/mpatankar/met-museum/issues/28)) ([c262da1](https://github.com/mpatankar/met-museum/commit/c262da1ce712380b7d060751430282affb71f91a))
* **internal:** codegen related update ([b9a78ff](https://github.com/mpatankar/met-museum/commit/b9a78ff2b8a1b3e7234802ca1515199865ca5e6e))
* **internal:** codegen related update ([bd3d5eb](https://github.com/mpatankar/met-museum/commit/bd3d5eb5f1c40ec7eeb50c80c30ed7c9fa7b903f))
* **internal:** codegen related update ([3f0ffc4](https://github.com/mpatankar/met-museum/commit/3f0ffc47f34013abb7ff4b802bfee7a192306a53))
* **internal:** codegen related update ([e122225](https://github.com/mpatankar/met-museum/commit/e122225764f74395247cf375c977ed6147a5ee18))
* **internal:** codegen related update ([559bd49](https://github.com/mpatankar/met-museum/commit/559bd493a26245d58f4ea2e102766af5a459e723))
* **internal:** codegen related update ([7a1a2cd](https://github.com/mpatankar/met-museum/commit/7a1a2cd4d521be9d23db0bad0d556b8615f65c3e))
* **internal:** codegen related update ([3c10429](https://github.com/mpatankar/met-museum/commit/3c10429eb7287f84811e21caad34d269edb4a0fd))
* **internal:** codegen related update ([849fb76](https://github.com/mpatankar/met-museum/commit/849fb7673e9adc7ec8ac07aa69798a904d34fc9b))
* **internal:** codegen related update ([4ee6330](https://github.com/mpatankar/met-museum/commit/4ee6330e98695b02f53d241647907944bc8b4cee))
* **internal:** codegen related update ([d81034a](https://github.com/mpatankar/met-museum/commit/d81034a877c7208b8c7ecd6a073a4c35c18e709c))
* **internal:** codegen related update ([0c8ae93](https://github.com/mpatankar/met-museum/commit/0c8ae93eb58a8d4ea55b1df8726113cb27641716))
* **internal:** codegen related update ([7e6b2d1](https://github.com/mpatankar/met-museum/commit/7e6b2d1fefa76fdc6a880377e36898b6066082b8))
* **internal:** codegen related update ([b44318f](https://github.com/mpatankar/met-museum/commit/b44318fa8a7953a836fb1adde712d65bb9e2a682))
* **internal:** codegen related update ([6488259](https://github.com/mpatankar/met-museum/commit/6488259e197f5e49995f0362d1dc1c3a228224a1))
* **internal:** codegen related update ([cba2ab3](https://github.com/mpatankar/met-museum/commit/cba2ab336ebf39fb5733ef289ccce5b6c3abb482))
* **internal:** codegen related update ([#27](https://github.com/mpatankar/met-museum/issues/27)) ([b8315d2](https://github.com/mpatankar/met-museum/commit/b8315d2f7c5a02530da849c694a11f1a88a8b6de))
* **internal:** codegen related update ([#35](https://github.com/mpatankar/met-museum/issues/35)) ([4daa724](https://github.com/mpatankar/met-museum/commit/4daa7247599e36ce20825faa4c5570fc523757c0))
* **internal:** codegen related update ([#36](https://github.com/mpatankar/met-museum/issues/36)) ([ccd87c3](https://github.com/mpatankar/met-museum/commit/ccd87c30a4313cc56dfcfbdf6a405b00a0893f43))
* **internal:** detect breaking changes when removing endpoints ([46b7df2](https://github.com/mpatankar/met-museum/commit/46b7df27cf64cc964e62d879a73b0915451e3cac))
* **internal:** expand CI branch coverage ([6beecb0](https://github.com/mpatankar/met-museum/commit/6beecb008df501fbb637ab3dad2ae344f4c98fcf))
* **internal:** fix list file params ([b00ce85](https://github.com/mpatankar/met-museum/commit/b00ce851a6aa96649c8c85103a49e4b850d55095))
* **internal:** import reformatting ([9e0f163](https://github.com/mpatankar/met-museum/commit/9e0f163f6df86ec75b26152153415677620e1802))
* **internal:** minor formatting changes ([544d9d8](https://github.com/mpatankar/met-museum/commit/544d9d8cf303673f3a5b4674d667c39e86945204))
* **internal:** reduce CI branch coverage ([fa70fb0](https://github.com/mpatankar/met-museum/commit/fa70fb0bcf9470be7f7c0da58ee950151790db1e))
* **internal:** refactor retries to not use recursion ([28e163f](https://github.com/mpatankar/met-museum/commit/28e163f45b220372421b344b6805fd0920054c3b))
* **internal:** remove trailing character ([#34](https://github.com/mpatankar/met-museum/issues/34)) ([f6bf200](https://github.com/mpatankar/met-museum/commit/f6bf200e385574ec4fc3b3abed9858548c9840e5))
* **internal:** slight transform perf improvement ([#37](https://github.com/mpatankar/met-museum/issues/37)) ([c52830c](https://github.com/mpatankar/met-museum/commit/c52830c4dfe0c9e239e57c008ab7d56f73804fa4))
* **internal:** update comment in script ([3b1abb7](https://github.com/mpatankar/met-museum/commit/3b1abb7c3c6d44ed4429e173517ef193eebee0b2))
* **internal:** update models test ([7465553](https://github.com/mpatankar/met-museum/commit/74655534b3d965c265723ff58b2c341ad757c477))
* **internal:** update pyright settings ([d9d364d](https://github.com/mpatankar/met-museum/commit/d9d364df90b716381e6e06e727bdd86ac033ae4c))
* update SDK settings ([09abdf0](https://github.com/mpatankar/met-museum/commit/09abdf02b2f7667f4b2061f207e593e57d7813ec))

## 1.4.0 (2025-03-14)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/mpatankar/met-museum/compare/v1.3.0...v1.4.0)

### Features

* **client:** add endpoint for listing objects ([#22](https://github.com/mpatankar/met-museum/issues/22)) ([6dea04e](https://github.com/mpatankar/met-museum/commit/6dea04e4f25fc7e174bd8c0e2f35fc6b583dc091))

## 1.3.0 (2025-03-14)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/mpatankar/met-museum/compare/v1.2.0...v1.3.0)

### Features

* **client:** add list endpoint ([#17](https://github.com/mpatankar/met-museum/issues/17)) ([8ddd58f](https://github.com/mpatankar/met-museum/commit/8ddd58f257dd5451e26dda00d9613d2d3dfe6d4d))
* **client:** make search title optional ([#19](https://github.com/mpatankar/met-museum/issues/19)) ([62c8a1c](https://github.com/mpatankar/met-museum/commit/62c8a1cff2ff7aa5cc37c5741d8d8a656c05a1c1))
* **client:** make search title required ([#18](https://github.com/mpatankar/met-museum/issues/18)) ([f241b52](https://github.com/mpatankar/met-museum/commit/f241b52d2cb4301852a6c2cd2649dbd262ee7e5a))
* **client:** remove list endpoint ([#15](https://github.com/mpatankar/met-museum/issues/15)) ([ab5b0b3](https://github.com/mpatankar/met-museum/commit/ab5b0b3551d94a16a14ba8255a464ab1160c3928))
* **client:** remove list endpoint ([#20](https://github.com/mpatankar/met-museum/issues/20)) ([8b31c7c](https://github.com/mpatankar/met-museum/commit/8b31c7c4c416ff79f615e41f92fba5e84385b470))

## 1.2.0 (2025-03-14)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/mpatankar/met-museum/compare/v1.1.0...v1.2.0)

### Features

* **client:** add a list endpoint ([#12](https://github.com/mpatankar/met-museum/issues/12)) ([6e6641f](https://github.com/mpatankar/met-museum/commit/6e6641f4b076d81edef007ca525a3a1dd3dac67a))

## 1.1.0 (2025-03-14)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/mpatankar/met-museum/compare/v1.0.0...v1.1.0)

### Features

* Update ci.yml ([195e6ed](https://github.com/mpatankar/met-museum/commit/195e6edf2b6727cae142bc678edf31c5b651ed8c))


### Chores

* **internal:** version bump ([#9](https://github.com/mpatankar/met-museum/issues/9)) ([59fd5aa](https://github.com/mpatankar/met-museum/commit/59fd5aa3691d0f2b4c523c051c4a90c7e4719519))

## 1.0.0 (2025-03-14)

Full Changelog: [v0.1.0-alpha.1...v1.0.0](https://github.com/mpatankar/met-museum/compare/v0.1.0-alpha.1...v1.0.0)

### Features

* **api:** update via SDK Studio ([#4](https://github.com/mpatankar/met-museum/issues/4)) ([a360baf](https://github.com/mpatankar/met-museum/commit/a360bafeb7af06562fcd43d5f4420d03175017df))
* **api:** update via SDK Studio ([#6](https://github.com/mpatankar/met-museum/issues/6)) ([03d3412](https://github.com/mpatankar/met-museum/commit/03d34124a106d8558285b72c549bb0629a50014b))
* **api:** update via SDK Studio ([#7](https://github.com/mpatankar/met-museum/issues/7)) ([52b9e24](https://github.com/mpatankar/met-museum/commit/52b9e24c47909f949672b52f5bee469529e41a97))
* **api:** update via SDK Studio ([#8](https://github.com/mpatankar/met-museum/issues/8)) ([2359f83](https://github.com/mpatankar/met-museum/commit/2359f83e288c577026e1a453539b75c088d5026a))

## 0.1.0-alpha.1 (2025-03-14)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/mpatankar/met-museum/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([b984c7c](https://github.com/mpatankar/met-museum/commit/b984c7ced8519cca492a2a9f3855a59d50fc78ae))
* **api:** update via SDK Studio ([47d021c](https://github.com/mpatankar/met-museum/commit/47d021ceeceb6a0a442a65f64e65f7bd73027dff))
* **api:** update via SDK Studio ([13e1b73](https://github.com/mpatankar/met-museum/commit/13e1b7331e321c8736802424cd85afd79f68b984))
* **api:** update via SDK Studio ([84743b5](https://github.com/mpatankar/met-museum/commit/84743b5d64a023eb202cc063db50aa22447dfa11))
* **api:** update via SDK Studio ([cb6bde0](https://github.com/mpatankar/met-museum/commit/cb6bde07c4e0de6a9e8085d11c2a9aca61b8f43d))
* **api:** update via SDK Studio ([fafff44](https://github.com/mpatankar/met-museum/commit/fafff4495b6b64a978d883049abfa1fba2768088))
* **api:** update via SDK Studio ([0683fb2](https://github.com/mpatankar/met-museum/commit/0683fb2914116754aeb85ca311f47547c1223429))
* **api:** update via SDK Studio ([6d3c86d](https://github.com/mpatankar/met-museum/commit/6d3c86dfdc893120aaaed22a999a6f588106705c))
* **client:** allow passing `NotGiven` for body ([46a04c6](https://github.com/mpatankar/met-museum/commit/46a04c63c4b42b36e6fa966bab5eedcabbdb4a0a))
* **client:** send `X-Stainless-Read-Timeout` header ([35dfcaf](https://github.com/mpatankar/met-museum/commit/35dfcaf1cdaa7484bd77ad1ba6308e4f03b52839))


### Bug Fixes

* asyncify on non-asyncio runtimes ([9749303](https://github.com/mpatankar/met-museum/commit/9749303483287ccd18cdc1b78de7dec208fbbf6e))
* **client:** compat with new httpx 0.28.0 release ([02cad6b](https://github.com/mpatankar/met-museum/commit/02cad6b5c8a04a339f5251548796b93cf1a986f9))
* **client:** mark some request bodies as optional ([46a04c6](https://github.com/mpatankar/met-museum/commit/46a04c63c4b42b36e6fa966bab5eedcabbdb4a0a))


### Chores

* add missing isclass check ([d9b3f96](https://github.com/mpatankar/met-museum/commit/d9b3f965a18f15ee8ca0365463b1a0aaea886b04))
* **docs:** update client docstring ([134eb86](https://github.com/mpatankar/met-museum/commit/134eb86029c5c4d18adac8b705dfd7f1bf6d6c3e))
* go live ([#1](https://github.com/mpatankar/met-museum/issues/1)) ([77b3389](https://github.com/mpatankar/met-museum/commit/77b338962c7867e85016e539b46b5d94fda6e5c9))
* **internal:** add support for TypeAliasType ([51b1a0d](https://github.com/mpatankar/met-museum/commit/51b1a0d94b72123c8753425fe9066750b0a3fde8))
* **internal:** bummp ruff dependency ([17b2b9b](https://github.com/mpatankar/met-museum/commit/17b2b9b0c95c0f8f3951c06676c64cd9bf2d9533))
* **internal:** bump httpx dependency ([10f7b4c](https://github.com/mpatankar/met-museum/commit/10f7b4c79f9a3bd2f6a317ab07826585c4d009c9))
* **internal:** bump pydantic dependency ([6bcf427](https://github.com/mpatankar/met-museum/commit/6bcf4277b131539c8b530c72f4ff7b1e80cd21bf))
* **internal:** bump pyright ([0583f29](https://github.com/mpatankar/met-museum/commit/0583f290d31a5efbee66fe07be778b163b0cad48))
* **internal:** bump pyright ([fb90ba5](https://github.com/mpatankar/met-museum/commit/fb90ba554eeb57b77d2766324cf141c977935156))
* **internal:** change default timeout to an int ([296a8fc](https://github.com/mpatankar/met-museum/commit/296a8fc84d2afdae212dfd167113930b57a91116))
* **internal:** codegen related update ([1f8f76c](https://github.com/mpatankar/met-museum/commit/1f8f76cbbe0d03f6426906d83ae85f5d3ca8d090))
* **internal:** codegen related update ([9d9fcae](https://github.com/mpatankar/met-museum/commit/9d9fcaef6d8c0c4143df4183e4769d8551adbb76))
* **internal:** codegen related update ([ef36008](https://github.com/mpatankar/met-museum/commit/ef36008a7ea884eba9b6f61c257f75ef490f5822))
* **internal:** codegen related update ([43c1dab](https://github.com/mpatankar/met-museum/commit/43c1dab5f8e4f1534e87e48288c021809e9d14a8))
* **internal:** codegen related update ([e1cefbe](https://github.com/mpatankar/met-museum/commit/e1cefbe02b7eb0c10075700bf08c88485bb6f9f5))
* **internal:** codegen related update ([7866126](https://github.com/mpatankar/met-museum/commit/786612690e1dccbbdfa2961d3e2d3d13ce06d027))
* **internal:** codegen related update ([e5ecb3b](https://github.com/mpatankar/met-museum/commit/e5ecb3b2ba43a94576de4eb745af774e92c895a1))
* **internal:** codegen related update ([dc5b6fd](https://github.com/mpatankar/met-museum/commit/dc5b6fd5661e67465af5cef09a13a6c1bea299eb))
* **internal:** codegen related update ([a82971a](https://github.com/mpatankar/met-museum/commit/a82971a24b3f69027e81869167502b264081bd68))
* **internal:** exclude mypy from running on tests ([6119107](https://github.com/mpatankar/met-museum/commit/61191077922a88b873f4bea70652799f8596a85c))
* **internal:** fix compat model_dump method when warnings are passed ([81bd0ba](https://github.com/mpatankar/met-museum/commit/81bd0ba936f2f93242e38b3e341d0475c63dab86))
* **internal:** fix devcontainers setup ([25e2a32](https://github.com/mpatankar/met-museum/commit/25e2a3273616f5e2374fd3c3762b0a8bbfa4e541))
* **internal:** fix some typos ([fbfd3b5](https://github.com/mpatankar/met-museum/commit/fbfd3b5a3a61af5a57b35a597139730de1bada9e))
* **internal:** fix type traversing dictionary params ([1251c3e](https://github.com/mpatankar/met-museum/commit/1251c3e21b6574f703fd5fa10e0cdcf1658fe8f5))
* **internal:** minor formatting changes ([ace74e3](https://github.com/mpatankar/met-museum/commit/ace74e3dbf364b0798de92e3aa47e11c14f7bb3d))
* **internal:** minor type handling changes ([2588f27](https://github.com/mpatankar/met-museum/commit/2588f277d9a5e8274e4e9fd6cdfb8d24e31c16e8))
* **internal:** properly set __pydantic_private__ ([51be963](https://github.com/mpatankar/met-museum/commit/51be963f71a888f5973d6de18d514a093a0deb00))
* **internal:** remove extra empty newlines ([bf41e64](https://github.com/mpatankar/met-museum/commit/bf41e649ac663ae6f8801a93bd287d88527c0122))
* **internal:** remove unused http client options forwarding ([e05958c](https://github.com/mpatankar/met-museum/commit/e05958c61068208d24586e38857b85098520907f))
* make the `Omit` type public ([fcc1cb5](https://github.com/mpatankar/met-museum/commit/fcc1cb51014e73fedae9012bb610bcf5bc26e66f))
* rebuild project due to codegen change ([fb4b371](https://github.com/mpatankar/met-museum/commit/fb4b371f5e950d7c10d212f65cca62616d6d31b3))
* rebuild project due to codegen change ([3b10e21](https://github.com/mpatankar/met-museum/commit/3b10e21c3c641b5a2d067b5f31a33350e46a41bb))
* rebuild project due to codegen change ([e5d3157](https://github.com/mpatankar/met-museum/commit/e5d3157959f5a6cb8b35a0f47cf82569733eede6))
* remove now unused `cached-property` dep ([7202a9b](https://github.com/mpatankar/met-museum/commit/7202a9b4df70da3a46d528e4eabe4f837bc8fa7d))


### Documentation

* add info log level to readme ([152dbbc](https://github.com/mpatankar/met-museum/commit/152dbbcee0f0ea56491765d0174caca28937b123))
* **readme:** example snippet for client context manager ([7123c0e](https://github.com/mpatankar/met-museum/commit/7123c0e670d8d881c0f64192d737ea082bc4d713))
* **readme:** fix http client proxies example ([32803f6](https://github.com/mpatankar/met-museum/commit/32803f66905dbd7639d7f9011e3f4c5bf274a829))
* update URLs from stainlessapi.com to stainless.com ([b16881f](https://github.com/mpatankar/met-museum/commit/b16881f3a189968ec12182e52f53bc8e6868cd57))
