#ifndef LIGHTBLUEOBEX_MAIN_H
#define LIGHTBLUEOBEX_MAIN_H

#include "Python.h"
#include <openobex/obex.h>

/* compatibility with python versions before 2.5 (PEP 353) */
#if PY_VERSION_HEX < 0x02050000 && !defined(PY_SSIZE_T_MIN)
typedef int Py_ssize_t;
#define PY_SSIZE_T_MAX INT_MAX
#define PY_SSIZE_T_MIN INT_MIN
#endif


#ifndef LIGHTBLUE_DEBUG
#define LIGHTBLUE_DEBUG 0
#endif

#if LIGHTBLUE_DEBUG
#define DEBUG(format, args...) fprintf(stderr, format, ##args)
#else
#define DEBUG(format, args...)
#endif


PyObject *lightblueobex_readheaders(obex_t *obex, obex_object_t *obj);

int lightblueobex_addheaders(obex_t *obex, PyObject *headers, obex_object_t *obj);

PyObject *lightblueobex_filetostream(obex_t *obex, obex_object_t *obj, PyObject *fileobj, int bufsize);

int lightblueobex_streamtofile(obex_t *obex, obex_object_t *obj, PyObject *fileobj);

#endif
