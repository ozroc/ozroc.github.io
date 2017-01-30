Title: Ola de ataques de ransomware: ¿pone en entredicho la seguridad de MongoDB y otras bases de datos libres?
Slug: randomware-mongodb
Date: 2017-01-30 00:00
Category: posts
Tags: security, mongodb, free software, open source
Author: Pablo Manuel García Corzo
picture: /images/microwavecat.png


Se están leyendo estos días multitud de noticias acerca de ataques ransomware a determinadas bases de datos como <a href="http://www.itworldcanada.com/article/ransomware-attacks-on-insecure-hadoop-systems-may-be-next-say-security-researchers/389944">Hadoop</a>, <a href="http://www.cbronline.com/news/cybersecurity/breaches/mongodb-elasticsearch-hackers-now-target-hadoop-ransomware/">ElasticSearch</a>, <a href="https://www.bleepingcomputer.com/news/security/database-ransom-attacks-hit-couchdb-and-hadoop-servers/">Couchdb</a> o <a href="http://www.theregister.co.uk/2017/01/04/mongodb_installs_wiped_by_bitcoin_ransoming_script/">MongoDB</a> y en algunos medios <a href="http://www.elconfidencial.com/tecnologia/2017-01-10/mongodb-hackers-ataque-informatico-bases-datos-servidores_1314168/">se relacionan los ataques con el hecho de que se trate en todos esos casos de productos de software libre</a>.

Relacionar los recientes ataques con el hecho de que se trate de software libre o privativo no es acertado. Si atendemos a los detalles, los atacantes no se están aprovechando de ningún tipo de agujero de seguridad en estos productos, tan solo de configuraciones deficientes.

El problema real detrás de los recientes casos es sencillamente un problema de inversión. Hay históricamente mucha tendencia a asimilar software libre como sinónimo de software gratuito, pero esto es un gran error de concepto contra el que el mundo del software libre lleva luchando muchos años. En inglés, donde la ambigüedad del término “free software” ha alimentado la confusión, se suele hablar de este tema diferenciando entre software “free as in freedom but not as in free beer”.

> Es cierto que una empresa en ocasiones puede ahorrar costes usando software libre y desplegándolo sobre sus propios sistemas, pero eso significa responsabilizarse de la configuración y posterior mantenimiento de sus productos.

Evidentemente, en muchos casos integrar un equipo de expertos para una necesidad puntual no encaja con el modelo de negocio de la empresa. En estos casos siempre se puede delegar esa tarea bien contratando el servicio a un tercero o acudiendo a un servicio en la nube (léase el caso de <a href="https://www.mongodb.com/cloud/atlas">Atlas</a> para MongoDB, por ejemplo).

El caso de los ataques ransomware que salen estos días a la luz, es el de una hipotética empresa que ha apostado por ahorrarse todos los costes posibles montando un producto de software libre por sí misma (cosa absolutamente legítima) pero sin contar con la experiencia y el conocimiento necesarios para configurar correctamente la aplicación y llevar a cabo una auditoría de seguridad.

Digo esto porque los ataques que se han dado han sido sobre instalaciones sin securizar. No estamos hablando de tomar medidas de precaución adicionales como proteger las bases de datos tras un cortafuegos, sino de seguir <a href="https://docs.mongodb.com/manual/security/">las instrucciones de securización</a> reflejadas en el manual del producto. El resultado, a fin de cuentas, es que se han dejado esas bases de datos completamente abiertas a Internet y sin que sea necesaria una simple password para acceder a ellas.

> Si dejas abiertas de par en par las puertas de tu casa y entran los ladrones no significa que tu casa sea insegura. Es tu responsabilidad. A nadie se le ocurriría pedir cuentas al fabricante de la cerradura de la puerta en un caso así.

Otra cosa sería que se hubieran descubierto vulnerabilidades reales con las que el ladrón puede de verdad saltarse la seguridad de una plataforma correctamente configurada. Eso puede suceder y sucede en cualquier producto (independientemente de que sea <a href="https://www.cvedetails.com/vulnerability-list/vendor_id-12752/product_id-25450/Mongodb-Mongodb.html">libre</a> o <a href="https://www.cvedetails.com/vulnerability-list/vendor_id-93/product_id-467/cvssscoremin-5/cvssscoremax-5.99/Oracle-Database-Server.html">privativo</a>) y ante estas incidencias no hay más prevención posible que mantener al día las actualizaciones de seguridad liberadas por los desarrolladores.
En general y por la propia naturaleza del software de código abierto, es más difícil que esto suceda en software libre que en productos privativos. Cuando el código de tu producto es accesible a cualquiera, los protocolos de seguridad han de ser reales.

>Liberar el código significa enseñar a los posibles ladrones los planos de tu casa en los que se detalla el tipo de alarmas instaladas o la cerradura que tienes en la puerta.

El sistema debe ser seguro por diseño y suele haber una verdadera comunidad de observadores imparciales, expertos en la materia, que no dudan en señalar los eventuales defectos para que sean solucionados.
En el caso del software privativo, esos observadores dejan de ser imparciales, porque sólo los empleados de la empresa tienen acceso al código del producto. En algunos casos las empresas se cobijan sencillamente en que el secreto protege de que los ladrones encuentren esos agujeros de seguridad y los utilicen, pero esos problemas suelen terminar apareciendo tarde o temprano.

En definitiva, lo que estos casos ponen de manifiesto no es un problema de seguridad intrínseco a los productos de software libre, sino un problema de responsabilidad de los usuarios de los mismos.

> Si pretendiéramos responsabilizar de algún modo a MongoDB o a otro de los productos afectados por estos casos de ransomware sólo les podríamos exigir introducir notas en sus manuales acercándonos al paradigmático extremo de especificar que no se debe introducir un gato en el microondas.
