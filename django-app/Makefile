BUILDDIR=~test
test: clean
	cookiecutter . -o ${BUILDDIR} --no-input -f \
		&& cd ${BUILDDIR}/application-name \
		&& git add . \
		&& make develop \
		&& make lint \
		&& pytest tests \
		&& tox

clean:
	rm -fr ${BUILDDIR}
