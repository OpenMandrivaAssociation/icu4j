
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		icu4j
Epoch:		1
Version:	50.1.1
Release:	2.2
License:	GPLv3+
Source0:	icu4j-50.1.1-2.2-omv2014.0.noarch.rpm
Source1:	icu4j-charset-50.1.1-2.2-omv2014.0.noarch.rpm
Source2:	icu4j-eclipse-50.1.1-2.2-omv2014.0.noarch.rpm
Source3:	icu4j-javadoc-50.1.1-2.2-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/icu4j
BuildArch:	noarch
Summary:	icu4j bootstrap version
Requires:	javapackages-bootstrap
Requires:	java >= 1:1.6.0
Requires:	jpackage-utils
Provides:	icu4j = 1:50.1.1-2.2:2014.0
Provides:	mvn(com.ibm.icu:icu4j) = 50.1.1
Provides:	osgi(com.ibm.icu) = 50.1.1

%description
icu4j bootstrap version.

%files
/usr/share/doc/icu4j
/usr/share/doc/icu4j/APIChangeReport.html
/usr/share/doc/icu4j/readme.html
/usr/share/java/icu4j.jar
/usr/share/maven-fragments/icu4j
/usr/share/maven-poms/JPP-icu4j.pom

#------------------------------------------------------------------------
%package	-n icu4j-charset
Epoch:		1
Version:	50.1.1
Release:	2.2
Summary:	icu4j-charset bootstrap version
Requires:	javapackages-bootstrap
Requires:	jpackage-utils
Provides:	icu4j-charset = 1:50.1.1-2.2:2014.0
Provides:	osgi(com.ibm.icu.charset) = 50.1.1

%description	-n icu4j-charset
icu4j-charset bootstrap version.

%files		-n icu4j-charset
/usr/share/java/icu4j-charset.jar

#------------------------------------------------------------------------
%package	-n icu4j-eclipse
Epoch:		1
Version:	50.1.1
Release:	2.2
Summary:	icu4j-eclipse bootstrap version
Requires:	javapackages-bootstrap
Requires:	jpackage-utils
Provides:	icu4j-eclipse = 1:50.1.1-2.2:2014.0
Provides:	osgi(com.ibm.icu) = 50.1.1
Provides:	osgi(com.ibm.icu.source) = 50.1.1

%description	-n icu4j-eclipse
icu4j-eclipse bootstrap version.

%files		-n icu4j-eclipse
/usr/share/doc/icu4j-eclipse
/usr/share/doc/icu4j-eclipse/readme.html
/usr/share/java/icu4j-eclipse
/usr/share/java/icu4j-eclipse/features
/usr/share/java/icu4j-eclipse/features/com.ibm.icu_50.1.1.v20130412
/usr/share/java/icu4j-eclipse/features/com.ibm.icu_50.1.1.v20130412/feature.xml
/usr/share/java/icu4j-eclipse/plugins
/usr/share/java/icu4j-eclipse/plugins/com.ibm.icu.source_50.1.1.v20130412.jar
/usr/share/java/icu4j-eclipse/plugins/com.ibm.icu_50.1.1.v20130412.jar

#------------------------------------------------------------------------
%package	-n icu4j-javadoc
Epoch:		1
Version:	50.1.1
Release:	2.2
Summary:	icu4j-javadoc bootstrap version
Requires:	javapackages-bootstrap
Requires:	java-javadoc >= 1:1.6.0
Requires:	jpackage-utils
Provides:	icu4j-javadoc = 1:50.1.1-2.2:2014.0

%description	-n icu4j-javadoc
icu4j-javadoc bootstrap version.

%files		-n icu4j-javadoc
/usr/share/javadoc/icu4j
/usr/share/javadoc/icu4j/allclasses-frame.html
/usr/share/javadoc/icu4j/allclasses-noframe.html
/usr/share/javadoc/icu4j/com
/usr/share/javadoc/icu4j/com/ibm
/usr/share/javadoc/icu4j/com/ibm/icu
/usr/share/javadoc/icu4j/com/ibm/icu/charset
/usr/share/javadoc/icu4j/com/ibm/icu/charset/CharsetCallback.Decoder.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/CharsetCallback.Encoder.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/CharsetCallback.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/CharsetDecoderICU.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/CharsetEncoderICU.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/CharsetICU.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/CharsetProviderICU.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/CharsetSelector.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/class-use
/usr/share/javadoc/icu4j/com/ibm/icu/charset/class-use/CharsetCallback.Decoder.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/class-use/CharsetCallback.Encoder.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/class-use/CharsetCallback.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/class-use/CharsetDecoderICU.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/class-use/CharsetEncoderICU.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/class-use/CharsetICU.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/class-use/CharsetProviderICU.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/class-use/CharsetSelector.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/package-frame.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/package-summary.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/package-tree.html
/usr/share/javadoc/icu4j/com/ibm/icu/charset/package-use.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang
/usr/share/javadoc/icu4j/com/ibm/icu/lang/CharSequences.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.DecompositionType.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.EastAsianWidth.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.GraphemeClusterBreak.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.HangulSyllableType.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.JoiningGroup.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.JoiningType.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.LineBreak.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.NumericType.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.SentenceBreak.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.UnicodeBlock.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.WordBreak.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacter.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacterCategory.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacterDirection.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacterEnums.ECharacterCategory.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacterEnums.ECharacterDirection.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UCharacterEnums.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UProperty.NameChoice.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UProperty.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UScript.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/UScriptRun.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/CharSequences.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.DecompositionType.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.EastAsianWidth.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.GraphemeClusterBreak.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.HangulSyllableType.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.JoiningGroup.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.JoiningType.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.LineBreak.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.NumericType.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.SentenceBreak.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.UnicodeBlock.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.WordBreak.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacter.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacterCategory.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacterDirection.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacterEnums.ECharacterCategory.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacterEnums.ECharacterDirection.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UCharacterEnums.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UProperty.NameChoice.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UProperty.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UScript.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/class-use/UScriptRun.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/package-frame.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/package-summary.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/package-tree.html
/usr/share/javadoc/icu4j/com/ibm/icu/lang/package-use.html
/usr/share/javadoc/icu4j/com/ibm/icu/math
/usr/share/javadoc/icu4j/com/ibm/icu/math/BigDecimal.html
/usr/share/javadoc/icu4j/com/ibm/icu/math/MathContext.html
/usr/share/javadoc/icu4j/com/ibm/icu/math/class-use
/usr/share/javadoc/icu4j/com/ibm/icu/math/class-use/BigDecimal.html
/usr/share/javadoc/icu4j/com/ibm/icu/math/class-use/MathContext.html
/usr/share/javadoc/icu4j/com/ibm/icu/math/package-frame.html
/usr/share/javadoc/icu4j/com/ibm/icu/math/package-summary.html
/usr/share/javadoc/icu4j/com/ibm/icu/math/package-tree.html
/usr/share/javadoc/icu4j/com/ibm/icu/math/package-use.html
/usr/share/javadoc/icu4j/com/ibm/icu/text
/usr/share/javadoc/icu4j/com/ibm/icu/text/AlphabeticIndex.Bucket.LabelType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/AlphabeticIndex.Bucket.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/AlphabeticIndex.Record.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/AlphabeticIndex.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/ArabicShaping.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/ArabicShapingException.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Bidi.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/BidiClassifier.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/BidiRun.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/BreakIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CanonicalIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CharsetDetector.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CharsetMatch.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/ChineseDateFormat.Field.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/ChineseDateFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/ChineseDateFormatSymbols.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CollationElementIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CollationKey.BoundMode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CollationKey.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Collator.CollatorFactory.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Collator.ReorderCodes.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Collator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CompactDecimalFormat.CompactStyle.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CompactDecimalFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/ComposedCharIter.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CurrencyDisplayNames.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CurrencyMetaInfo.CurrencyDigits.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CurrencyMetaInfo.CurrencyFilter.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CurrencyMetaInfo.CurrencyInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CurrencyMetaInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/CurrencyPluralInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DateFormat.Field.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DateFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DateFormatSymbols.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DateIntervalFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DateIntervalInfo.PatternInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DateIntervalInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DateTimePatternGenerator.FormatParser.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DateTimePatternGenerator.PatternInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DateTimePatternGenerator.VariableField.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DateTimePatternGenerator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DecimalFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DecimalFormatSymbols.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DisplayContext.Type.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DisplayContext.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/DurationFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/FilteredNormalizer2.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/IDNA.Error.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/IDNA.Info.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/IDNA.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/ListFormatter.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/LocaleDisplayNames.DialectHandling.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/LocaleDisplayNames.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MeasureFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessageFormat.Field.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessageFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePattern.ApostropheMode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePattern.ArgType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePattern.Part.Type.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePattern.Part.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePattern.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePatternUtil.ArgNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePatternUtil.ComplexArgStyleNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePatternUtil.MessageContentsNode.Type.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePatternUtil.MessageContentsNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePatternUtil.MessageNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePatternUtil.Node.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePatternUtil.TextNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePatternUtil.VariantNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/MessagePatternUtil.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Normalizer.Mode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Normalizer.QuickCheckResult.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Normalizer.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Normalizer2.Mode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Normalizer2.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/NumberFormat.Field.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/NumberFormat.NumberFormatFactory.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/NumberFormat.SimpleNumberFormatFactory.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/NumberFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/NumberingSystem.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/PluralFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/PluralRules.KeywordStatus.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/PluralRules.PluralType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/PluralRules.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/RawCollationKey.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/RbnfLenientScanner.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/RbnfLenientScannerProvider.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/RbnfScannerProviderImpl.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Replaceable.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/ReplaceableString.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/RuleBasedBreakIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/RuleBasedCollator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/RuleBasedNumberFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/RuleBasedTransliterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/SearchIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/SelectFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/SimpleDateFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/SpoofChecker.Builder.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/SpoofChecker.CheckResult.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/SpoofChecker.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/StringCharacterIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/StringPrep.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/StringPrepParseException.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/StringSearch.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/StringTransform.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/SymbolTable.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/TimeUnitFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/TimeZoneFormat.GMTOffsetPatternType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/TimeZoneFormat.ParseOption.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/TimeZoneFormat.Style.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/TimeZoneFormat.TimeType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/TimeZoneFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/TimeZoneNames.Factory.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/TimeZoneNames.MatchInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/TimeZoneNames.NameType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/TimeZoneNames.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Transform.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Transliterator.Factory.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Transliterator.Position.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/Transliterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UCharacterIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UForwardCharacterIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UTF16.StringComparator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UTF16.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UnicodeCompressor.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UnicodeDecompressor.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UnicodeFilter.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UnicodeMatcher.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UnicodeSet.ComparisonStyle.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UnicodeSet.SpanCondition.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UnicodeSet.XSymbolTable.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UnicodeSet.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/UnicodeSetIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/AlphabeticIndex.Bucket.LabelType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/AlphabeticIndex.Bucket.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/AlphabeticIndex.Record.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/AlphabeticIndex.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/ArabicShaping.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/ArabicShapingException.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Bidi.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/BidiClassifier.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/BidiRun.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/BreakIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CanonicalIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CharsetDetector.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CharsetMatch.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/ChineseDateFormat.Field.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/ChineseDateFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/ChineseDateFormatSymbols.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CollationElementIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CollationKey.BoundMode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CollationKey.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Collator.CollatorFactory.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Collator.ReorderCodes.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Collator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CompactDecimalFormat.CompactStyle.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CompactDecimalFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/ComposedCharIter.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CurrencyDisplayNames.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CurrencyMetaInfo.CurrencyDigits.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CurrencyMetaInfo.CurrencyFilter.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CurrencyMetaInfo.CurrencyInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CurrencyMetaInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/CurrencyPluralInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DateFormat.Field.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DateFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DateFormatSymbols.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DateIntervalFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DateIntervalInfo.PatternInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DateIntervalInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DateTimePatternGenerator.FormatParser.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DateTimePatternGenerator.PatternInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DateTimePatternGenerator.VariableField.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DateTimePatternGenerator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DecimalFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DecimalFormatSymbols.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DisplayContext.Type.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DisplayContext.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/DurationFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/FilteredNormalizer2.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/IDNA.Error.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/IDNA.Info.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/IDNA.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/ListFormatter.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/LocaleDisplayNames.DialectHandling.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/LocaleDisplayNames.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MeasureFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessageFormat.Field.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessageFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePattern.ApostropheMode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePattern.ArgType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePattern.Part.Type.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePattern.Part.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePattern.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePatternUtil.ArgNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePatternUtil.ComplexArgStyleNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePatternUtil.MessageContentsNode.Type.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePatternUtil.MessageContentsNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePatternUtil.MessageNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePatternUtil.Node.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePatternUtil.TextNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePatternUtil.VariantNode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/MessagePatternUtil.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Normalizer.Mode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Normalizer.QuickCheckResult.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Normalizer.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Normalizer2.Mode.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Normalizer2.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/NumberFormat.Field.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/NumberFormat.NumberFormatFactory.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/NumberFormat.SimpleNumberFormatFactory.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/NumberFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/NumberingSystem.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/PluralFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/PluralRules.KeywordStatus.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/PluralRules.PluralType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/PluralRules.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/RawCollationKey.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/RbnfLenientScanner.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/RbnfLenientScannerProvider.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/RbnfScannerProviderImpl.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Replaceable.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/ReplaceableString.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/RuleBasedBreakIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/RuleBasedCollator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/RuleBasedNumberFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/RuleBasedTransliterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/SearchIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/SelectFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/SimpleDateFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/SpoofChecker.Builder.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/SpoofChecker.CheckResult.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/SpoofChecker.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/StringCharacterIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/StringPrep.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/StringPrepParseException.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/StringSearch.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/StringTransform.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/SymbolTable.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/TimeUnitFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/TimeZoneFormat.GMTOffsetPatternType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/TimeZoneFormat.ParseOption.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/TimeZoneFormat.Style.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/TimeZoneFormat.TimeType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/TimeZoneFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/TimeZoneNames.Factory.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/TimeZoneNames.MatchInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/TimeZoneNames.NameType.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/TimeZoneNames.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Transform.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Transliterator.Factory.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Transliterator.Position.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/Transliterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UCharacterIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UFormat.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UForwardCharacterIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UTF16.StringComparator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UTF16.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UnicodeCompressor.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UnicodeDecompressor.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UnicodeFilter.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UnicodeMatcher.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UnicodeSet.ComparisonStyle.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UnicodeSet.SpanCondition.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UnicodeSet.XSymbolTable.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UnicodeSet.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/class-use/UnicodeSetIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/package-frame.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/package-summary.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/package-tree.html
/usr/share/javadoc/icu4j/com/ibm/icu/text/package-use.html
/usr/share/javadoc/icu4j/com/ibm/icu/util
/usr/share/javadoc/icu4j/com/ibm/icu/util/AnnualTimeZoneRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/BasicTimeZone.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/BuddhistCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/ByteArrayWrapper.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/BytesTrie.Entry.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/BytesTrie.Iterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/BytesTrie.Result.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/BytesTrie.State.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/BytesTrie.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/BytesTrieBuilder.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/Calendar.FormatConfiguration.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/Calendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/CaseInsensitiveString.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/CharsTrie.Entry.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/CharsTrie.Iterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/CharsTrie.State.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/CharsTrie.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/CharsTrieBuilder.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/ChineseCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/CompactByteArray.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/CompactCharArray.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/CopticCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/Currency.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/CurrencyAmount.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/DangiCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/DateInterval.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/DateRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/DateTimeRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/EasterHoliday.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/EthiopicCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/Freezable.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/GenderInfo.Gender.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/GenderInfo.ListGenderStyle.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/GenderInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/GlobalizationPreferences.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/GregorianCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/HebrewCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/HebrewHoliday.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/Holiday.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/IllformedLocaleException.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/IndianCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/InitialTimeZoneRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/IslamicCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/JapaneseCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/LocaleData.MeasurementSystem.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/LocaleData.PaperSize.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/LocaleData.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/LocaleMatcher.LanguageMatcherData.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/LocaleMatcher.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/LocalePriorityList.Builder.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/LocalePriorityList.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/Measure.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/MeasureUnit.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/Output.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/OverlayBundle.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/PersianCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/RangeDateRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/RangeValueIterator.Element.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/RangeValueIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/Region.RegionType.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/Region.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/RuleBasedTimeZone.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/SimpleDateRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/SimpleHoliday.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/SimpleTimeZone.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/StringTokenizer.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/StringTrieBuilder.Option.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/StringTrieBuilder.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/TaiwanCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/TimeArrayTimeZoneRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/TimeUnit.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/TimeUnitAmount.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/TimeZone.SystemTimeZoneType.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/TimeZone.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/TimeZoneRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/TimeZoneTransition.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/ULocale.Builder.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/ULocale.Category.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/ULocale.Type.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/ULocale.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/UResourceBundle.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/UResourceBundleIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/UResourceTypeMismatchException.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/UniversalTimeScale.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/VTimeZone.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/ValueIterator.Element.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/ValueIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/VersionInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/AnnualTimeZoneRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/BasicTimeZone.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/BuddhistCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/ByteArrayWrapper.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/BytesTrie.Entry.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/BytesTrie.Iterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/BytesTrie.Result.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/BytesTrie.State.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/BytesTrie.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/BytesTrieBuilder.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/Calendar.FormatConfiguration.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/Calendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/CaseInsensitiveString.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/CharsTrie.Entry.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/CharsTrie.Iterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/CharsTrie.State.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/CharsTrie.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/CharsTrieBuilder.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/ChineseCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/CompactByteArray.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/CompactCharArray.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/CopticCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/Currency.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/CurrencyAmount.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/DangiCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/DateInterval.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/DateRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/DateTimeRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/EasterHoliday.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/EthiopicCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/Freezable.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/GenderInfo.Gender.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/GenderInfo.ListGenderStyle.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/GenderInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/GlobalizationPreferences.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/GregorianCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/HebrewCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/HebrewHoliday.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/Holiday.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/IllformedLocaleException.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/IndianCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/InitialTimeZoneRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/IslamicCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/JapaneseCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/LocaleData.MeasurementSystem.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/LocaleData.PaperSize.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/LocaleData.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/LocaleMatcher.LanguageMatcherData.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/LocaleMatcher.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/LocalePriorityList.Builder.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/LocalePriorityList.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/Measure.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/MeasureUnit.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/Output.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/OverlayBundle.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/PersianCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/RangeDateRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/RangeValueIterator.Element.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/RangeValueIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/Region.RegionType.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/Region.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/RuleBasedTimeZone.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/SimpleDateRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/SimpleHoliday.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/SimpleTimeZone.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/StringTokenizer.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/StringTrieBuilder.Option.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/StringTrieBuilder.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/TaiwanCalendar.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/TimeArrayTimeZoneRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/TimeUnit.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/TimeUnitAmount.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/TimeZone.SystemTimeZoneType.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/TimeZone.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/TimeZoneRule.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/TimeZoneTransition.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/ULocale.Builder.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/ULocale.Category.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/ULocale.Type.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/ULocale.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/UResourceBundle.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/UResourceBundleIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/UResourceTypeMismatchException.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/UniversalTimeScale.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/VTimeZone.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/ValueIterator.Element.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/ValueIterator.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/class-use/VersionInfo.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/package-frame.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/package-summary.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/package-tree.html
/usr/share/javadoc/icu4j/com/ibm/icu/util/package-use.html
/usr/share/javadoc/icu4j/constant-values.html
/usr/share/javadoc/icu4j/help-doc.html
/usr/share/javadoc/icu4j/index-all.html
/usr/share/javadoc/icu4j/index.html
/usr/share/javadoc/icu4j/overview-frame.html
/usr/share/javadoc/icu4j/overview-summary.html
/usr/share/javadoc/icu4j/overview-tree.html
/usr/share/javadoc/icu4j/package-list
/usr/share/javadoc/icu4j/resources
/usr/share/javadoc/icu4j/resources/background.gif
/usr/share/javadoc/icu4j/resources/tab.gif
/usr/share/javadoc/icu4j/resources/titlebar.gif
/usr/share/javadoc/icu4j/resources/titlebar_end.gif
/usr/share/javadoc/icu4j/serialized-form.html
/usr/share/javadoc/icu4j/stylesheet.css

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
rpm2cpio %{SOURCE2} | cpio -id
rpm2cpio %{SOURCE3} | cpio -id
