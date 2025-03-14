# Changelog

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
