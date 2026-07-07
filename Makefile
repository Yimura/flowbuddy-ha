.PHONY: regen test lint typecheck ci

SPEC := openapi/flexmon-v1.json
SPEC_URL := https://izen.cast4all.energy/flexMon/v1/openapi.json
GEN_DIR := custom_components/flowbuddy/_generated

regen:
	@sha_new=$$(sha256sum $(SPEC) | awk '{print $$1}'); \
	sha_recorded=$$(cat $(SPEC).sha256); \
	if [ "$$sha_new" != "$$sha_recorded" ]; then \
		echo "ERROR: $(SPEC) sha256 does not match $(SPEC).sha256"; \
		echo "  recorded: $$sha_recorded"; \
		echo "  actual:   $$sha_new"; \
		exit 1; \
	fi
	rm -rf $(GEN_DIR)
	mkdir -p $(dir $(GEN_DIR))
	python -m openapi_python_client generate \
		--path $(SPEC) \
		--output-path $(GEN_DIR) \
		--overwrite \
		--meta none
	ruff format $(GEN_DIR)
	ruff check --fix --unsafe-fixes $(GEN_DIR) || true
	@echo '"""Auto-generated FlexMon v1 client. DO NOT EDIT — run \`make regen\`."""' > $(GEN_DIR)/__init__.py
	@echo 'spec_version = "V1.0.0"' >> $(GEN_DIR)/__init__.py
	@echo 'spec_sha256 = "'$$(cat $(SPEC).sha256)'"' >> $(GEN_DIR)/__init__.py

test:
	pytest --cov

lint:
	ruff check .
	ruff format --check .

typecheck:
	mypy custom_components/flowbuddy

ci: lint typecheck test
