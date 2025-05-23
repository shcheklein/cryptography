# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import annotations

INCLUDES = """
#include <openssl/ssl.h>

/*
 * This is part of a work-around for the difficulty cffi has in dealing with
 * `STACK_OF(foo)` as the name of a type.  We invent a new, simpler name that
 * will be an alias for this type and use the alias throughout.  This works
 * together with another opaque typedef for the same name in the TYPES section.
 * Note that the result is an opaque type.
 */
typedef STACK_OF(X509) Cryptography_STACK_OF_X509;
"""

TYPES = """
typedef ... Cryptography_STACK_OF_X509;

typedef ... X509_ALGOR;
typedef ... X509_EXTENSION;
typedef ... X509_EXTENSIONS;
typedef ... X509_REQ;
typedef ... X509_CRL;
typedef ... X509;

typedef void (*sk_X509_EXTENSION_freefunc)(X509_EXTENSION *);
"""

FUNCTIONS = """
X509 *X509_new(void);
void X509_free(X509 *);
X509 *X509_dup(X509 *);
int X509_up_ref(X509 *);

int X509_print_ex(BIO *, X509 *, unsigned long, unsigned long);

int X509_set_version(X509 *, long);

EVP_PKEY *X509_get_pubkey(X509 *);
int X509_set_pubkey(X509 *, EVP_PKEY *);

int X509_sign(X509 *, EVP_PKEY *, const EVP_MD *);

int X509_digest(const X509 *, const EVP_MD *, unsigned char *, unsigned int *);

ASN1_TIME *X509_gmtime_adj(ASN1_TIME *, long);

unsigned long X509_subject_name_hash(X509 *);

int X509_set_subject_name(X509 *, X509_NAME *);

int X509_set_issuer_name(X509 *, X509_NAME *);

int X509_add_ext(X509 *, X509_EXTENSION *, int);
X509_EXTENSION *X509_EXTENSION_dup(X509_EXTENSION *);

ASN1_OBJECT *X509_EXTENSION_get_object(X509_EXTENSION *);
void X509_EXTENSION_free(X509_EXTENSION *);

int X509_REQ_set_version(X509_REQ *, long);
X509_REQ *X509_REQ_new(void);
void X509_REQ_free(X509_REQ *);
int X509_REQ_set_pubkey(X509_REQ *, EVP_PKEY *);
int X509_REQ_sign(X509_REQ *, EVP_PKEY *, const EVP_MD *);
int X509_REQ_verify(X509_REQ *, EVP_PKEY *);
EVP_PKEY *X509_REQ_get_pubkey(X509_REQ *);
int X509_REQ_print_ex(BIO *, X509_REQ *, unsigned long, unsigned long);
int X509_REQ_add_extensions(X509_REQ *, X509_EXTENSIONS *);
X509_EXTENSIONS *X509_REQ_get_extensions(X509_REQ *);

int X509V3_EXT_print(BIO *, X509_EXTENSION *, unsigned long, int);
ASN1_OCTET_STRING *X509_EXTENSION_get_data(X509_EXTENSION *);

X509_CRL *d2i_X509_CRL_bio(BIO *, X509_CRL **);
void X509_CRL_free(X509_CRL *);

/*  ASN1 serialization */
int i2d_X509_bio(BIO *, X509 *);
X509 *d2i_X509_bio(BIO *, X509 **);

int i2d_X509_REQ_bio(BIO *, X509_REQ *);
X509_REQ *d2i_X509_REQ_bio(BIO *, X509_REQ **);

int i2d_PrivateKey_bio(BIO *, EVP_PKEY *);
EVP_PKEY *d2i_PrivateKey_bio(BIO *, EVP_PKEY **);
int i2d_PUBKEY_bio(BIO *, EVP_PKEY *);
EVP_PKEY *d2i_PUBKEY_bio(BIO *, EVP_PKEY **);

ASN1_INTEGER *X509_get_serialNumber(X509 *);
int X509_set_serialNumber(X509 *, ASN1_INTEGER *);

const char *X509_verify_cert_error_string(long);

const char *X509_get_default_cert_dir(void);
const char *X509_get_default_cert_file(void);

int X509_get_ext_count(const X509 *);
X509_EXTENSION *X509_get_ext(const X509 *, int);
X509_NAME *X509_get_subject_name(const X509 *);
X509_NAME *X509_get_issuer_name(const X509 *);

int X509_EXTENSION_get_critical(const X509_EXTENSION *);

const X509_ALGOR *X509_get0_tbs_sigalg(const X509 *);

long X509_get_version(X509 *);

ASN1_TIME *X509_getm_notBefore(const X509 *);
ASN1_TIME *X509_getm_notAfter(const X509 *);

long X509_REQ_get_version(X509_REQ *);
X509_NAME *X509_REQ_get_subject_name(X509_REQ *);

Cryptography_STACK_OF_X509 *sk_X509_new_null(void);
void sk_X509_free(Cryptography_STACK_OF_X509 *);
int sk_X509_num(Cryptography_STACK_OF_X509 *);
int sk_X509_push(Cryptography_STACK_OF_X509 *, X509 *);
X509 *sk_X509_value(Cryptography_STACK_OF_X509 *, int);

X509_EXTENSIONS *sk_X509_EXTENSION_new_null(void);
int sk_X509_EXTENSION_num(X509_EXTENSIONS *);
X509_EXTENSION *sk_X509_EXTENSION_value(X509_EXTENSIONS *, int);
int sk_X509_EXTENSION_push(X509_EXTENSIONS *, X509_EXTENSION *);
void sk_X509_EXTENSION_free(X509_EXTENSIONS *);
void sk_X509_EXTENSION_pop_free(X509_EXTENSIONS *, sk_X509_EXTENSION_freefunc);

void X509_ALGOR_get0(const ASN1_OBJECT **, int *, const void **,
                     const X509_ALGOR *);
"""

CUSTOMIZATIONS = """
"""
